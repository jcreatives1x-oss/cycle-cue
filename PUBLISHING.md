# Publishing Cycle Cue

Claude prepares and fills in everything it can. The steps marked **YOU** need your own login, payment or ID, which the stores only accept from the account owner.

## 1. Accounts (start now, verification takes days)

| | What | Cost | Who |
|---|---|---|---|
| A | Apple Developer Program, developer.apple.com/programs | $99/year | **YOU** |
| B | Google Play Console, play.google.com/console | $25 once | **YOU** |
| C | GitHub account, github.com | Free | **YOU** |

Google Play: new personal accounts must run a closed test with 12 testers for 14 straight days before the app can go to production. Line up 12 Android users with Gmail addresses.

## 2. Put the code on GitHub

1. **YOU:** create a new repository named `cycle-cue` (it can be public or private), then connect GitHub to Claude, or upload this folder in the browser with "Add file" → "Upload files".
2. Claude: replaces `[CONTACT_EMAIL]` and the privacy link in the app, pushes the code and turns on GitHub Pages from the `docs` folder. That makes the support and privacy URLs live.

## 3. Android

1. **YOU:** add three repository secrets (Settings → Secrets and variables → Actions). The values are in the private signing zip:
   `ANDROID_KEYSTORE_BASE64`, `ANDROID_KEYSTORE_PASSWORD`, `ANDROID_KEY_ALIAS`
2. Claude: runs the "Android build" workflow, which produces `cycle-cue.aab`.
3. **YOU:** sign in to Play Console and click "Create app". Claude can then fill in the listing, data safety form, content rating, health declaration and target audience, using `STORE-LISTING.md`.
4. Claude: uploads the first `.aab` to a Closed testing track. **YOU:** add the 12 testers' emails and share the opt-in link with them.
5. After 14 days: apply for production access in Play Console (a short questionnaire Claude can draft), then submit for review.

Optional: create a Play service account with release permission and save its JSON as `PLAY_SERVICE_ACCOUNT_JSON`. Every later build then uploads itself.

## 4. iOS (no Mac needed)

1. **YOU:** in App Store Connect → Users and Access → Integrations → App Store Connect API, create a key with the **Admin** role. Download the `.p8` file (it can only be downloaded once).
2. **YOU:** add four repository secrets:
   - `ASC_KEY_ID`: the key ID shown next to the key
   - `ASC_ISSUER_ID`: shown at the top of that page
   - `ASC_KEY_P8_BASE64`: the `.p8` file, base64-encoded (Claude can convert it if you attach it)
   - `APPLE_TEAM_ID`: Membership details on developer.apple.com
3. **YOU:** in App Store Connect, click Apps → "+" → New App. Use the bundle ID `com.olufunto.cyclecue` and the name from `STORE-LISTING.md`.
4. Claude: runs the "iOS build" workflow. It builds in the cloud, signs and uploads to TestFlight.
5. Claude: fills in the listing, privacy label, age rating and review notes. **YOU:** click "Submit for Review". Apple usually responds within 1–3 days.

## Updating the app later

Edit `www/index.html`, then push a tag such as `v1.0.1`. Both workflows build again, and you submit the new version in each store.

## Before you change the bundle ID

`com.olufunto.cyclecue` is set in `capacitor.config.json` and `.github/workflows/android.yml`. Change both before the first upload if you want a different ID. After the first upload it can never change.
