from pathlib import Path
import json,random,runpy
root=Path(__file__).resolve().parents[1];base=json.loads((root/'tools/base_content.json').read_text());rng=random.Random(20261021)
d=base;concepts=d['concepts'];EXAMPLES=runpy.run_path(str(root/'tools/context_examples.py'))['EXAMPLES'];CASES=runpy.run_path(str(root/'tools/exam_cases.py'))['CASES']
extra=[
(1,'Communicative language choice','Selection of language resources in relation to audience, purpose, access and opportunity.','A child uses Punjabi with a willing grandparent and Urdu with a teacher, adjusting to the communication partner.','All bilingual children first choose between languages at exactly two and a half years.','Audience-sensitive use develops through experience; the slide age is not a universal onset rule.'),
(4,'Multiple levels of language','Organization across related levels such as sounds or signs, meaningful parts, words, sentences and discourse.','An Urdu expression can be examined for its sounds, word parts, sentence organization and intended meaning.','Multiply structured means every language has exactly the same sounds and word order.','The handout does not define multiply structured precisely. Study organization across levels; duality of patterning is one related, more specific distinction.'),
(4,'Semantics','The organization and interpretation of linguistic meaning, including word meanings and relationships.','A preschool child learns that several particular items belong to the broader category clothing and uses more precise descriptions.','Learning more word meanings alone completely explains every change in grammatical complexity.','Vocabulary, conceptual relationships, grammar and discourse develop together; semantic growth is relevant without being the sole cause of complexity.'),
(5,'Regional labels within Hindko','Names associated with regional Hindko varieties, including Kohat- and Peshawar-related labels in relevant descriptions.','A clinician records a family\'s preferred regional label and language history instead of assuming that all Hindko use is uniform.','Kohati and Peshawari labels establish one identical Punjabi variety in every northern district.','The handout groups labels broadly. Specify the source and community identification; do not infer exact boundaries, uniformity or uncontested taxonomy.')]
for lec,term,definition,example,false,note in extra:
 n=1+sum(c['lecture']==lec for c in concepts)
 concepts.append(dict(id=f'LM{lec}-C{n:02d}',lecture=lec,term=term,definition=definition,example=example,false=false,note=note,origin='Supplementary clarification of handout',sourceIds=next(c['sourceIds'] for c in concepts if c['lecture']==lec),referenceSection='Clarification of the supplied deck; see the slide coverage map.'))
# Explicit clusters place commonly confused concepts together. Each comparison uses the actual definitions.
clusters=[
['Language','Speech and language','Signed language'],['Monolingualism','Bilingualism','Multilingualism','Trilingualism','Polyglot'],['Individual multilingualism','Societal multilingualism'],['Simultaneous bilingual acquisition','Sequential bilingual acquisition'],['Early bilingualism','Late bilingualism','Age of acquisition'],['Receptive bilingualism','Productive bilingual ability'],['Dominant bilingualism','Balanced bilingualism'],['Additive bilingualism','Subtractive bilingualism'],['Heritage language','Majority language','Minority language'],['First language','Additional language'],['Language repertoire','Language domain','Communicative language choice'],['Receptive language','Expressive language'],['Biliteracy','Unimodal bilingualism','Bimodal bilingualism'],['Code-switching','Code-mixing','Borrowing','Translanguaging'],['Cross-linguistic influence','Cross-language generalization'],['Language maintenance','Language shift','Language attrition'],['Metalinguistic awareness','Cognitive-advantage evidence','Executive-function claim'],['Distributed vocabulary','Language history','Historical semilingualism label'],
['Bilingual-development myth','Language difference','Language disorder'],['Language exposure','Responsive interaction'],['Home-language support','One-person-one-language approach','Minority-language-at-home approach'],['Mixed-language interaction','Complementarity principle'],['Language-of-intervention planning','Bilingual intervention approach','Cross-linguistic intervention approach'],['Shared linguistic feature','Contrastive analysis'],['Cross-language generalization','Within-language generalization'],['Concept-based teaching','Functional vocabulary'],['Narrative intervention','Repetitive language framework','Interest-based intervention'],['Caregiver coaching','Home practice'],['Progress monitoring','Baseline probe'],['Language sampling','Dynamic assessment','Modifiability'],['Conceptual vocabulary scoring','Total vocabulary scoring'],['Appropriate normative comparison','Dialect-informed assessment'],['Interpreter','Translator','Cultural broker'],['Hearing consideration','Functional participation goal','Family-centered decision'],['Accommodation','Assimilation'],['Assimilation in schema theory','Accommodation in schema theory'],
['Second-language acquisition','Proficiency continuum'],['Pre-production stage','Silent period','Early production stage'],['Speech emergence stage','Intermediate fluency stage','Advanced fluency stage','Stage-model limitation'],['Basic interpersonal communicative skills (BICS)','Cognitive academic language proficiency (CALP)'],['Common underlying proficiency (CUP)','Iceberg metaphor','Transfer condition'],['Context-embedded communication','Context-reduced communication'],['Cognitive demand','Context-demand matrix'],['Scaffolding','Visual support','Comprehensible input'],['Meaningful interaction','Negotiation of meaning','Clarification request'],['Wait time','Language-learning anxiety','Motivation'],['Academic vocabulary','Disciplinary language'],['Narrative genre','Expository genre'],['Inference','Synthesis'],['Prior knowledge','Formative assessment','Language-learning goal'],['Social benefit of bilingualism','Identity and bilingualism'],
['Culture','Idealist view of culture','Materialist emphasis in culture','Omnibus view of culture'],['Anthropology','Linguistic anthropology','Franz Boas'],['Dynamic culture','Within-group variation'],['Culture and nationality','Culture and religion','Culture and racialization','Ethnicity','Cultural identity'],['Language and culture','Linguistic relativity'],['Arbitrariness of signs','Meaningful structure'],['Duality of patterning','Multiple levels of language','Productivity'],['Language change','Communicative function','Language socialization'],['Pragmatics','Semantics'],['Phonetic perceptual tuning','Early vocabulary variation','Telegraphic speech','Later language development'],['Sociolinguistics','Social variation'],['Age-related variation','Gender and language','Social class and education','Ethnolect'],['African American English','Negative concord','Variable copula absence'],['Taboo','Linguistic taboo','Euphemism','Dysphemism'],['Nonverbal communication','Proxemics','Eye-contact interpretation','Intercultural communication'],['Cultural humility','Cultural responsiveness','Ethnocentrism','Stereotype','Cultural clarification'],['Proverb','Idiom','Humor in communication'],['Culture: word history','Culture'],
['Dialect','Accent','Language variety'],['Regional dialect','Sociolect','Idiolect','Regiolect and topolect'],['Standard dialect','Nonstandard dialect'],['Standardization','Codification'],['Overt prestige','Covert prestige'],['Speech community','Community of practice','Social network'],['Register','Jargon','Style shifting'],['Accommodation theory','Convergence','Divergence'],['Dialect continuum','Mutual intelligibility','Isogloss'],['Linguistic discrimination','Bidialectal repertoire','Dialect-informed assessment'],['Voice quality and idiolect','Idiolect'],['Shahpuri','Jhangochi or Jhangvi','Jangli and Rachnavi','Majhi'],['Malwai or Malwi','Doabi'],['Pahari-Pothwari','Derawali','Saraiki classification'],['Hindko','Regional labels within Hindko','Thali or Thalochi','Chenavari'],['Vitality','Historicity','Autonomy','Reduction','Mixture','De facto norms'],['Language ideology','Age grading','Language policy','Language revitalization','Language endangerment'],['Dialect: word history','Dialect']]
lookup={c['term']:c for c in concepts};related={}
for group in clusters:
 for i,t in enumerate(group):
  assert t in lookup,t
  if t not in related:related[t]=group[(i+1)%len(group)]
assert not(set(lookup)-set(related)),set(lookup)-set(related)
for c in concepts:
 c['originalExample']=c['example']
 if c['term'] in EXAMPLES:c['example'],c['exampleReason']=EXAMPLES[c['term']]
 else:c['exampleReason']=c['note']
 other=lookup[related[c['term']]]
 c['compareWith']=other['id'];c['comparison']=f"{c['term']}: {c['definition']} {other['term']}: {other['definition']}"
 c['retrievalPrompt']='Explain the concept in your own words, identify the evidence in the example, and distinguish it from '+other['term']+'.'
 c['modelAnswer']=c['definition']+' Example: '+c['example']+' Explanation: '+c['exampleReason']
 c['firstQuestionId']=f"LM{c['lecture']}-{(int(c['id'].split('C')[1])-1)*4+1:03d}"
# Retain canonical options for existing concepts, so retained progress stays meaningful.
questions=[q for q in d['questions'] if q.get('conceptId') and q['type']!='Statement evaluation']
for c in concepts[-4:]:
 group=[x for x in concepts if x['lecture']==c['lecture'] and x['id']!=c['id']];wrong=rng.sample(group,3)
 for v,(stem,opts,kind,level) in enumerate([
  ('Which concept matches this description?\n'+c['definition'],[c['term']]+[x['term'] for x in wrong],'Definition','Easy'),
  ('Which concept is most directly illustrated?\n'+c['example'],[c['term']]+[x['term'] for x in wrong],'Scenario application','Moderate'),
  ('Which claim needs correction in the context of '+c['term']+'?',[c['false'],c['definition'],c['note'],'An example is: '+c['example']],'Misconception check','Moderate')],1):
  order=list(range(4));rng.shuffle(order);questions.append(dict(id=f"LM{c['lecture']}-{(int(c['id'].split('C')[1])-1)*4+v:03d}",lecture=c['lecture'],conceptId=c['id'],topic=c['term'],question=stem,options=[opts[x] for x in order],answer=order.index(0),type=kind,difficulty=level,level=level,origin=c['origin'],sourceIds=c['sourceIds'],referenceSection=c['referenceSection']))
byid={c['id']:c for c in concepts}
for q in questions:
 c=byid[q['conceptId']]
 if q['type']=='Scenario application':q['question']='Which concept is most directly illustrated by this situation?\n'+c['example']
 q['explanation']=c['definition']+'\nWorked example: '+c['example']+'\nWhy this fits: '+c['exampleReason']+'\nImportant distinction: '+c['note']
 q['optionExplanations']=[]
 for j,opt in enumerate(q['options']):
  if opt in lookup:
   x=lookup[opt];why=x['definition']+(' This matches the defining evidence in the question.' if j==q['answer'] else ' This is a different focus from the defining evidence in this question.')
  elif q['type']=='Misconception check':why=('This is the inaccurate claim. '+c['note']) if j==q['answer'] else 'This is an accurate description or qualified illustration, so it is not the claim requiring correction.'
  else:why=c['note']
  q['optionExplanations'].append(why)
 q['examEligible']=False
for lec,rows in CASES.items():
 for i,(topic,stem,correct,w1,w2,w3,why,whywrong) in enumerate(rows,1):
  opts=[correct,w1,w2,w3];order=list(range(4));rng.shuffle(order);level='Moderate' if i%3==0 else 'Challenging'
  q=dict(id=f'LM{lec}-E{i:02d}',lecture=lec,topic=topic,question=stem,options=[opts[x] for x in order],answer=order.index(0),type='Exam-style case' if topic!='Statement appraisal' else 'Statement appraisal',difficulty=level,level=level,origin='Original hypothetical exam practice',sourceIds=next(c['sourceIds'] for c in concepts if c['lecture']==lec),referenceSection='Original teaching case based on this module. See the slide map and Reading guide.',explanation=why+'\nWhy the alternatives do not follow: '+whywrong,optionExplanations=[why if x==0 else whywrong for x in order],examEligible=True)
  # Relevant concepts are navigable even when the question integrates more than one.
  matched=[c for c in concepts if c['lecture']==lec and (c['term'].lower() in (topic+' '+stem).lower() or topic.lower() in c['term'].lower())]
  q['relatedConceptIds']=[c['id'] for c in matched[:4]]
  questions.append(q)
ranks={'Easy':0,'Moderate':1,'Challenging':2};questions.sort(key=lambda q:(q['lecture'],ranks[q['difficulty']]))
d['questions']=questions;d['version']=2
for l in d['lectures']:
 l['count']=sum(q['lecture']==l['id'] for q in questions);l['concepts']=sum(c['lecture']==l['id'] for c in concepts);l['examCount']=sum(q['lecture']==l['id'] and q['examEligible'] for q in questions)
d['sources'] += [dict(id='milestones',title='ASHA — Communication Milestones: 19 to 24 Months',url='https://www.asha.org/public/developmental-milestones/communication-milestones-19-to-24-months/',use='Professional developmental guidance supporting careful correction of the slide’s rigid two-word-combination timeline; milestones inform review rather than replace individual assessment.'),dict(id='nbme',title='NBME — Item-Writing Guide',url='https://www.nbme.org/institutions/nbme-item-writing-guide/',use='General item-writing principles informed review of focused one-best-answer cases. These original practice items are not official, endorsed or psychometrically validated NBME questions.')]
(root/'data.json').write_text(json.dumps(d,ensure_ascii=False,indent=2));(root/'data.js').write_text('window.COURSE = '+json.dumps(d,ensure_ascii=False,separators=(',',':'))+';\n')
print(len(questions),'questions',len(concepts),'concepts;',len(EXAMPLES),'expanded worked examples')
