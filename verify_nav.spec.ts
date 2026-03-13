import { test, expect } from '@playwright/test';

test('navigation links should be keyboard focusable', async ({ page }) => {
  await page.goto('file://' + process.cwd() + '/index.html');

  // Press Tab and see what gets focus
  await page.keyboard.press('Tab');
  const activeElement = await page.evaluate(() => document.activeElement?.tagName);
  console.log('First focused element:', activeElement);

  // The first focusable element should probably be the logo or the first link
  // But currently they might not be focusable at all.
});
