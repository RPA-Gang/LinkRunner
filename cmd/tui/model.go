package tui

import tea "github.com/charmbracelet/bubbletea"

type model struct {
}

func (m model) Init() tea.Cmd {
	return nil
}

func (m model) Update(msg tea.Msg) (tea.Model, tea.Cmd) {
	// TODO implement me
	panic("implement me")
}

func (m model) View() string {
	// TODO implement me
	panic("implement me")
}

func NewTuiModel() tea.Model {
	return model{}
}
