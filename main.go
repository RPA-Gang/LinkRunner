package main

import (
	"database/sql"

	"github.com/charmbracelet/log"
)

var (
	db *sql.DB
)

func main() {
	var err error
	db, err = sql.Open("sqlite3", "./vm.db")
	if err != nil {
		log.Error(err)
	}
}
