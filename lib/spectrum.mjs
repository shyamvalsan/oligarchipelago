// Published editorial rubric. These numbers are judgments, not probabilities.
export const DIMENSIONS = {
  leverage: {label:'Political leverage', weight:0.25},
  benefit: {label:'Preferential economic benefit', weight:0.25},
  exchange: {label:'Wealth–power feedback', weight:0.5},
};
export function scoreRubric(rubric) {
  if(!rubric || Object.keys(DIMENSIONS).some(k=>!Number.isInteger(rubric[k]?.level)||rubric[k].level<0||rubric[k].level>4))return null;
  return Math.round(Object.entries(DIMENSIONS).reduce((sum,[k,d])=>sum+rubric[k].level*d.weight,0)*25);
}
export function wealthPosition(billions,scale='log'){
  if(scale==='linear')return billions/1000;
  // sqrt(2.5 * 1000) = 50: a fixed $50B divider exactly bisects the log axis.
  return Math.log(billions/2.5)/Math.log(400);
}
export function wealthDivider(scale='log'){return scale==='linear'?500:50;}
export function plotGeometry(mobile=false){
  const W=mobile?700:1000,H=mobile?900:740,L=mobile?105:100,R=W-35,T=80,B=mobile?735:620;
  return {W,H,L,R,T,B,cx:(L+R)/2,cy:(T+B)/2};
}
export function spectrumLabel(record){
  if(record?.score==null)return 'Insufficient evidence to place';
  return `${record.score}/100 · editorial estimate`;
}
