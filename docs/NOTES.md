# Pomodoro Technique - 📝 Notes from the journey 🍅 by 🍅


## 🏷️ Labels

- ✅ done
- 🚧 WIP
- ❌ ERROR
- ⚠ TODO

## 🍅 Pomodoro 1

- ✅ should give an error message when something other than a string is passed
- ✅ should convert 'hello world' to 'HELLO WORLD'
- ✅ should convert 'HELLO WORLD' to 'hello world'
- ✅ should convert 'hello WORLD' to 'HELLO world'
- 🚧 should convert 'HeLLo WoRLD' to 'hEllO wOrld'
- ⚠ should convert '12345'       to '12345'                   // Non-alphabetical characters are unaffected
- ⚠ should convert '1a2b3c4d5e'  to '1A2B3C4D5E' # pragma: allowlist secret
- ⚠ should convert 'String.prototype.toAlternatingCase' to 'sTRING.PROTOTYPE.TOaLTERNATINGcASE'
