package server

import (
	"net/http"
	"net/http/httptest"
	"testing"
)

func TestAutoLoginRequiresAuthenticatedSessionAndSafeTarget(t *testing.T) {
	s := &Server{jwtKey: []byte("01234567890123456789012345678901")}
	token, err := signJWT(s.jwtKey)
	if err != nil {
		t.Fatal(err)
	}
	for _, tc := range []struct {
		name, target, authorization string
		want                        int
	}{
		{"anonymous", "/auto-login", "", http.StatusUnauthorized},
		{"invalid token", "/auto-login", "Bearer invalid", http.StatusUnauthorized},
		{"external redirect", "/auto-login?target=%2F%2Fevil.example", "Bearer " + token, http.StatusBadRequest},
		{"script injection", "/auto-login?target=%2F%3C%2Fscript%3E", "Bearer " + token, http.StatusBadRequest},
		{"valid session", "/auto-login?target=%2Ffunction%2Ftasks", "Bearer " + token, http.StatusOK},
	} {
		t.Run(tc.name, func(t *testing.T) {
			r := httptest.NewRequest(http.MethodGet, tc.target, nil)
			if tc.authorization != "" {
				r.Header.Set("Authorization", tc.authorization)
			}
			w := httptest.NewRecorder()
			s.autoLogin(w, r)
			if w.Code != tc.want {
				t.Fatalf("got status %d, want %d", w.Code, tc.want)
			}
		})
	}
}
