class A
  def initialize(name, level, hp, mp)
    @@name = name
    @@level = level
    @@hp = hp
    @@mp = mp
  end
  
  def get_name
    return @@name
  end
end

a = A.new("hiki", 17, 17, 17)
puts a.get_name
