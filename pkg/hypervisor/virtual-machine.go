package hypervisor

type VirtualMachine struct {
	Name         string `json:"name"`
	Environment  string `json:"environment"`
	Location     string `json:"location"`
	ResourceType string `json:"type"`
	ResourceUrl  string `json:"url"`
	Comments     string `json:"comments"`
}
