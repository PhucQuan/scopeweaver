package server

import (
	"os"
	"path/filepath"
	"testing"

	"github.com/Autumn-27/norma/skill"
)

func TestBundledStrixSkillsLoad(t *testing.T) {
	root := filepath.Join("..", "skills")
	registry, err := skill.LoadDir(root)
	if err != nil {
		t.Fatalf("load bundled skills: %v", err)
	}
	loaded := map[string]bool{}
	for _, entry := range registry.List() {
		loaded[filepath.Base(entry.Dir)] = true
	}
	for _, category := range []string{
		"analysis", "cloud", "custom", "frameworks", "protocols",
		"reconnaissance", "technologies", "tooling", "vulnerabilities",
	} {
		name := "strix-" + category
		if !loaded[name] {
			t.Errorf("skill %s was not loaded", name)
		}
		entries, err := os.ReadDir(filepath.Join(root, name, "references"))
		if err != nil || len(entries) == 0 {
			t.Errorf("skill %s has no references: %v", name, err)
		}
	}
}
