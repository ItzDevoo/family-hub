import asyncio,json,re
from pathlib import Path
from playwright.async_api import async_playwright
ROOT=Path(r'C:\Users\jusss\.uncorded\plugin-dev\family-hub')
async def main():
 async with async_playwright() as p:
  browser=await p.chromium.launch()
  page=await browser.new_page()
  errors=[]
  page.on('pageerror',lambda e:errors.append(str(e)))
  html=ROOT.joinpath('frontend/index.html').read_text(encoding='utf-8-sig')
  html=re.sub(r'<script.*?</script>','',html)
  html=html.replace('<link rel="stylesheet" href="styles.css">','<style>'+ROOT.joinpath('frontend/styles.css').read_text(encoding='utf-8-sig')+'</style>')
  await page.set_content(html)
  await page.evaluate('''() => {window.calls=[];const state={me:'parent',parent:true,admin:true,members:[{id:'kid',name:'Alex',user_id:'kid-account',parent:0}],chores:[{id:'c1',title:'Put away the dishes',notes:'Clean plates go on the lower shelf.',member_id:'kid',due:'2026-11-02',cents:500,status:'open'}],events:[{id:'e1',title:'Saturday soccer practice',category:'Sports',starts:Date.now(),ends:Date.now()+3600000,location:'Community park',notes:'Bring water and cleats.',author_id:'parent'}],online:[]}; window.UncodedPlugin={createPluginFrontend:async()=>({request:async(a,p)=>{window.calls.push({a,p});return a==='state'?state:{ok:true}},on:()=>{}})}}''')
  await page.add_script_tag(content='(async()=>{'+ROOT.joinpath('frontend/app.js').read_text(encoding='utf-8-sig')+'})()')
  await page.get_by_role('button',name='Chores',exact=True).click()
  await page.get_by_role('button',name='+ New chore',exact=True).click()
  assert not await page.get_by_label('Reward amount (USD)').is_visible()
  await page.get_by_role('switch').check()
  await page.get_by_label('Reward amount (USD)').fill('7.25')
  await page.get_by_label('Chore',exact=True).fill('Wash the car')
  await page.get_by_role('button',name='Create chore',exact=True).click()
  assert (await page.evaluate('window.calls.filter(x=>x.a==="saveChore").at(-1).p.cents'))==725
  await page.get_by_role('button',name='+ New chore',exact=True).click()
  await page.get_by_role('switch').check()
  await page.get_by_label('Reward amount (USD)').fill('9.00')
  await page.get_by_role('switch').uncheck()
  await page.get_by_label('Chore',exact=True).fill('Make the bed')
  await page.get_by_role('button',name='Create chore',exact=True).click()
  assert (await page.evaluate('window.calls.filter(x=>x.a==="saveChore").at(-1).p.cents'))==0
  for width in [320,390,768,1280]:
   await page.set_viewport_size({'width':width,'height':844})
   for tab in ['Overview','Chores','Calendar','Rewards','Family']:
    await page.get_by_role('button',name=tab,exact=True).click()
    assert await page.evaluate('document.documentElement.scrollWidth <= innerWidth'),f'Overflow: {width} {tab}'
   await page.get_by_role('button',name='Chores',exact=True).click()
   await page.get_by_role('button',name='+ New chore',exact=True).click()
   await page.get_by_role('switch').check()
   assert await page.get_by_label('Reward amount (USD)').is_visible()
   assert await page.evaluate('document.querySelector("dialog").scrollWidth <= innerWidth'),f'Dialog overflow: {width}'
   if width in [390,1280]:await page.screenshot(path=str(ROOT/f'tests/chore-{width}.png'))
   await page.get_by_role('button',name='Close form').click()
  assert not errors,errors
  print('PASS: paid/unpaid reward requests; five views and chore form at 320, 390, 768, 1280px; no horizontal overflow or browser errors.')
  await browser.close()
asyncio.run(main())
