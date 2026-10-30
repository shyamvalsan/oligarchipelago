// Deterministic layout for the Oligarchipelago map. Pure functions: no DOM, no network.
// Island size is net worth. Position is a seeded force layout. Nothing here invents a relationship:
// ties are either (a) a company named in Forbes' source-of-wealth field, or (b) a sourced record in data/ties.json.

export const MAP_W=2600, MAP_H=1700;
export const MODES={
  wealth:{label:'Wealth & ties',note:'The richest sit near the centre; linked fortunes are pulled together.'},
  country:{label:'By country',note:'Islands gather into one archipelago per citizenship.'},
  industry:{label:'By industry',note:'Islands gather by Forbes industry, whatever the flag.'},
};

// Only named companies count as a shared fortune; sector words ('retail', 'mining') never do.
const SHARED_ALLOW=new Set(['google','amazon','facebook','microsoft','walmart','koch','mars','chanel','bmw','tesla','spacex']);

export function hash(str){let h=2166136261;for(let i=0;i<str.length;i++){h^=str.charCodeAt(i);h=Math.imul(h,16777619);}return h>>>0;}
export function rng(seed){let s=seed>>>0||1;return()=>{s^=s<<13;s>>>=0;s^=s>>>17;s^=s<<5;s>>>=0;return s/4294967296;};}

export function radius(wealth){return 15+74*Math.sqrt(Math.max(wealth,0)/839);}

export function sharedCompanyTies(people){
  const by=new Map();
  for(const p of people)for(const raw of String(p.sourceOfWealth||'').split(/,\s*| and /)){
    const t=raw.trim().toLowerCase();
    if(!SHARED_ALLOW.has(t))continue;
    if(!by.has(t))by.set(t,[]);by.get(t).push(p);
  }
  const ties=[];
  for(const [company,list] of by)for(let i=0;i<list.length;i++)for(let j=i+1;j<list.length;j++)
    ties.push({a:list[i].id,b:list[j].id,kind:'shared-fortune',label:`Both list ${company.replace(/^./,c=>c.toUpperCase())} as the source of their wealth`,source:'Forbes 2026 source-of-wealth field',url:list[i].profileUrl,date:'2026-03-01',derived:true});
  return ties;
}

export function mergeTies(people,documented=[]){
  const ids=new Set(people.map(p=>p.id));
  const out=[],seen=new Set();
  for(const t of [...documented.filter(t=>t.opened!==false),...sharedCompanyTies(people)]){
    if(!ids.has(t.a)||!ids.has(t.b)||t.a===t.b)continue;
    const key=[t.a,t.b].sort().join('|')+'|'+t.kind+'|'+t.label;
    if(seen.has(key))continue;seen.add(key);out.push(t);
  }
  return out;
}

function anchors(people,key){
  const groups=new Map();
  for(const p of people){const k=key(p);if(!groups.has(k))groups.set(k,{k,total:0,sq:0});const g=groups.get(k);g.total+=p.wealth;g.sq+=Math.pow(radius(p.wealth)+24,2);}
  const list=[...groups.values()].sort((a,b)=>b.total-a.total);
  const out=new Map(),placed=[],cx=MAP_W/2,cy=MAP_H/2;
  for(const g of list){
    g.R=Math.sqrt(g.sq)*1.12;
    let pt={x:cx,y:cy};
    for(let t=0;placed.length;t+=.35){
      const d=40+t*38,a=t*2.399963;
      pt={x:cx+Math.cos(a)*d*1.25,y:cy+Math.sin(a)*d*.85};
      if(placed.every(q=>Math.hypot(q.x-pt.x,q.y-pt.y)>=q.R+g.R+70))break;
    }
    placed.push({...pt,R:g.R});out.set(g.k,pt);
  }
  return out;
}

export function layout(people,ties,mode='wealth'){
  const rand=rng(hash('oligarchipelago-'+mode));
  const A=mode==='industry'?anchors(people,p=>p.industry):anchors(people,p=>p.country);
  const cx=MAP_W/2,cy=MAP_H/2,maxW=Math.max(...people.map(p=>p.wealth));
  const nodes=people.map(p=>{
    const a=A.get(mode==='industry'?p.industry:p.country),r=radius(p.wealth);
    return {id:p.id,r,w:p.wealth,x:a.x+(rand()-.5)*160,y:a.y+(rand()-.5)*160,ax:a.x,ay:a.y,vx:0,vy:0};
  });
  const index=new Map(nodes.map((n,i)=>[n.id,i]));
  const springs=ties.map(t=>({i:index.get(t.a),j:index.get(t.b),k:t.derived?.014:.024})).filter(s=>s.i!=null&&s.j!=null);
  const gravity=mode==='wealth'?.0022:.00005,pull=mode==='wealth'?.0016:.03;
  for(let step=0;step<520;step++){
    const cool=1-step/560;
    for(const n of nodes){
      n.vx+=(n.ax-n.x)*pull;n.vy+=(n.ay-n.y)*pull;
      const rich=Math.pow(n.w/maxW,.5);
      n.vx+=(cx-n.x)*gravity*(.25+rich*3);n.vy+=(cy-n.y)*gravity*(.25+rich*3);
    }
    for(const s of springs){
      const a=nodes[s.i],b=nodes[s.j],dx=b.x-a.x,dy=b.y-a.y,d=Math.hypot(dx,dy)||1,rest=a.r+b.r+80,f=(d-rest)*s.k;
      a.vx+=dx/d*f;a.vy+=dy/d*f;b.vx-=dx/d*f;b.vy-=dy/d*f;
    }
    for(let i=0;i<nodes.length;i++)for(let j=i+1;j<nodes.length;j++){
      const a=nodes[i],b=nodes[j];let dx=b.x-a.x,dy=b.y-a.y,d=Math.hypot(dx,dy)||.01;
      const min=a.r+b.r+44;
      if(d<min){const f=(min-d)/d*.5;dx*=f;dy*=f;a.x-=dx;a.y-=dy;b.x+=dx;b.y+=dy;}
    }
    for(const n of nodes){n.x+=n.vx*cool;n.y+=n.vy*cool;n.vx*=.55;n.vy*=.55;}
  }
  // final de-overlap pass so no two islands touch
  for(let pass=0;pass<60;pass++)for(let i=0;i<nodes.length;i++)for(let j=i+1;j<nodes.length;j++){
    const a=nodes[i],b=nodes[j];let dx=b.x-a.x,dy=b.y-a.y,d=Math.hypot(dx,dy)||.01,min=a.r+b.r+40;
    if(d<min){const f=(min-d)/d*.5;a.x-=dx*f;a.y-=dy*f;b.x+=dx*f;b.y+=dy*f;}
  }
  const xs=nodes.flatMap(n=>[n.x-n.r,n.x+n.r]),ys=nodes.flatMap(n=>[n.y-n.r,n.y+n.r]);
  return {nodes:Object.fromEntries(nodes.map(n=>[n.id,{x:n.x,y:n.y,r:n.r}])),bounds:{x0:Math.min(...xs),x1:Math.max(...xs),y0:Math.min(...ys),y1:Math.max(...ys)}};
}

// A closed, wobbly coastline as an SVG path, centred on 0,0. Seeded by id so it never changes between visits.
export function coastline(id,r,wobble=.26){
  const rand=rng(hash('coast-'+id)),n=14+Math.round(r/9);
  const ph=[rand()*6.28,rand()*6.28,rand()*6.28],amp=[.55,.3,.18];
  const pts=[];
  for(let i=0;i<n;i++){
    const a=i/n*Math.PI*2;
    let k=1;for(let h=0;h<3;h++)k+=wobble*amp[h]*Math.sin(a*(h+2)+ph[h])*2;
    k+=(rand()-.5)*.1;
    pts.push([Math.cos(a)*r*k*(1+.12*Math.sin(ph[0])),Math.sin(a)*r*k*(.86+.1*Math.cos(ph[1]))]);
  }
  return smoothClosed(pts);
}
export function smoothClosed(pts){
  const n=pts.length,mid=(a,b)=>[(a[0]+b[0])/2,(a[1]+b[1])/2];
  let d=`M${mid(pts[n-1],pts[0]).map(v=>v.toFixed(1))}`;
  for(let i=0;i<n;i++){const m=mid(pts[i],pts[(i+1)%n]);d+=`Q${pts[i][0].toFixed(1)} ${pts[i][1].toFixed(1)} ${m[0].toFixed(1)} ${m[1].toFixed(1)}`;}
  return d+'Z';
}

// Little hill glyphs scattered inside an island, seeded. Count grows with size.
export function hills(id,r){
  const rand=rng(hash('hills-'+id)),count=Math.min(14,Math.floor(r/11)),out=[];
  for(let i=0;i<count;i++){
    const a=rand()*6.28,d=Math.sqrt(rand())*r*.58,s=3.2+rand()*3.6;
    out.push({x:Math.cos(a)*d,y:Math.sin(a)*d*.8,s});
  }
  return out;
}

export function neighbours(ties,id){
  return ties.filter(t=>t.a===id||t.b===id).map(t=>({other:t.a===id?t.b:t.a,tie:t}));
}
