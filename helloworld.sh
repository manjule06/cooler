echo "Hello World!"

name="Vaidehi"
echo "my name is $name"

echo -n "enter you age: "
read age
echo "my age is $age"

if [ "$age" -ge 18 ]; then
   echo "you are adult"
else
   echo "you are minor"
fi

echo "Counting from 1 to 5"
for i in {1..5}; do
    echo $i
done
