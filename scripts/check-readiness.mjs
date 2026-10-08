// Read-only, offline check. Does not publish, modify files, or grant approval.
import {readFile} from 'node:fs/promises';
import {researchReadiness} from '../lib/readiness.mjs';
import {launchUniverse,LAUNCH_COUNT,ARCHIVE_COUNT} from '../lib/universe.mjs';
const read=async name=>JSON.parse(await readFile(new URL('../data/'+name,import.meta.url),'utf8'));
const [data,evidence]=await Promise.all([read('billionaires.json'),read('assessments.json')]);
const archive=researchReadiness(data.people,evidence);
const launch=launchUniverse(data,evidence);
const report=researchReadiness(launch.data.people,launch.evidence,{expectedCount:LAUNCH_COUNT});
report.structuralErrors.push(...archive.structuralErrors.map(e=>'Archive: '+e));
report.blockers.push(...archive.structuralErrors.map(e=>'Archive: '+e));
report.researchGatePassed=report.blockers.length===0;
console.log(JSON.stringify({scope:{launch:LAUNCH_COUNT,archive:ARCHIVE_COUNT,selection:'First 200 entries in saved Forbes annual-list order; not a handpicked scored subset.'},...report,archiveCounts:archive.counts,manualReleaseChecks:[
  'User confirmation of the evidence model and public-facing content.',
  'Independent editorial review and source-reuse permission review.',
  'Public corrections process, accessibility and browser verification.',
  'Explicit approval of the specific GitHub repository and publishing plan.'
]},null,2));
process.exitCode=report.researchGatePassed?0:1;
