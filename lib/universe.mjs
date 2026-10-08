// User-approved scope reduction on 2026-10-08: launch with the Forbes top 200.
// Keep the complete 500-entry source and research archive intact.
export const LAUNCH_COUNT=200;
export const ARCHIVE_COUNT=500;

export function launchUniverse(data,evidence){
  if(!Array.isArray(data?.people)||data.people.length!==ARCHIVE_COUNT||new Set(data.people.map(p=>p.id)).size!==ARCHIVE_COUNT)
    throw new Error('Expected the complete 500-entry source archive.');
  const people=data.people.slice(0,LAUNCH_COUNT);
  const countries=new Set(people.map(p=>p.country));
  const profiles=Object.fromEntries(people.map(p=>{
    const a=evidence?.profiles?.[p.id];
    if(!a)throw new Error(`Missing launch assessment: ${p.id}`);
    return [p.id,a];
  }));
  return {
    data:{...data,people,countries:Object.fromEntries(Object.entries(data.countries).filter(([name])=>countries.has(name)))},
    evidence:{...evidence,profiles}
  };
}
