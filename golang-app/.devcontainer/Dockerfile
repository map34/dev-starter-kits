FROM golang:1.17.3
RUN go get -v golang.org/x/tools/gopls@latest \
    honnef.co/go/tools/...@latest \
    golang.org/x/lint/golint@latest \
    github.com/mgechev/revive@latest \
    github.com/uudashr/gopkgs/v2/cmd/gopkgs@latest \
    github.com/ramya-rao-a/go-outline@latest \
    github.com/go-delve/delve/cmd/dlv@latest \
    github.com/cweill/gotests/...@latest \
    github.com/josharian/impl@latest \
    github.com/fatih/gomodifytags@latest \
    github.com/golang/protobuf/protoc-gen-go@latest \
    && cp /go/bin/dlv /go/bin/dlv-dap