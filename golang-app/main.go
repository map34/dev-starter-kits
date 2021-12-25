package main

import (
	"log"

	"github.com/map34/httpserver/app"
)

func main() {
	serverOptions := app.ServerOptions{
		HTTPHostPort: "0.0.0.0:8080",
	}
	server, err := app.NewServer(&serverOptions)
	if err != nil {
		log.Fatal("Failed to create server", err)
	}

	if err := server.Start(); err != nil {
		log.Fatal("Could not start servers", err)
	}

	for status := range server.HealthCheckStatus() {
		log.Printf("Received HealthCheck status: %v\n", status)
	}
}
