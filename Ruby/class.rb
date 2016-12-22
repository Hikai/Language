class A
  def initalize(name, age, sex)
    @name = name
    @age = age
    @sex = sex
  end
  
  def print_info
    puts "#{@name}, #{@age}, #{@sex}"
end

aa = A.new("hiki", 12, "female")
aa.print_info