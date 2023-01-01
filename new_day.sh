# main() {
#     echo "Creating new day"
#     echo $0
#     echo $1
#     echo $2
# }

# main $argv

echo using year $1
echo day$2

mkdir -p $1/day$2
touch $1/day$2/input1
touch $1/day$2/part1.txt
touch $1/day$2/main.py
