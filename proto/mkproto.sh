mkdir -p ../server/pb
mkdir -p ../client/pb

protoc *.proto --python_out=../server/pb
protoc *.proto --python_out=../client/pb
