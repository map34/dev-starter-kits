package app

import (
	"log"
	"net"
	"net/http"

	"github.com/map34/httpserver/healthcheck"
	"github.com/rs/cors"
)

type ServerOptions struct {
	HTTPHostPort string
}

type Server struct {
	serverOptions      *ServerOptions
	httpConn           net.Listener
	httpServer         *http.Server
	unavailableChannel chan healthcheck.Status
}

func NewServer(serverOptions *ServerOptions) (*Server, error) {
	httpServer, err := createHttpServer()
	if err != nil {
		return nil, err
	}

	return &Server{
		serverOptions:      serverOptions,
		httpServer:         httpServer,
		unavailableChannel: make(chan healthcheck.Status),
	}, nil
}

func (server *Server) HealthCheckStatus() chan healthcheck.Status {
	return server.unavailableChannel
}

func (server *Server) initListener() error {
	var err error
	server.httpConn, err = net.Listen("tcp", server.serverOptions.HTTPHostPort)
	if err != nil {
		return err
	}
	return nil
}

func (server *Server) Start() error {
	err := server.initListener()
	if err != nil {
		return err
	}

	go func() {
		switch err := server.httpServer.Serve(server.httpConn); err {
		case nil, http.ErrServerClosed:
			// Normal Errors
		default:
			log.Println("Could not start HTTP server", err)
		}
		server.unavailableChannel <- healthcheck.Unavailable
	}()
	return nil
}

func createHttpServer() (*http.Server, error) {
	mux := http.NewServeMux()
	// TODO: Organize this to its own handler file
	mux.HandleFunc("/", func(w http.ResponseWriter, r *http.Request) {
		w.Header().Set("Content-Type", "application/json")
		w.Write([]byte("{\"hello\": \"world\"}"))
	})

	corsMiddleware := cors.New(cors.Options{
		AllowedOrigins: []string{"*"},
		AllowedMethods: []string{"GET", "DELETE", "POST", "PUT"},
	})

	return &http.Server{
		Handler: corsMiddleware.Handler(mux),
	}, nil
}
