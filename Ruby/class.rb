class A
  @@name = nil
  @@level = 0
  @@hp = 0
  @@mp = 0

  def initialize(name, level, hp, mp)
    @@name = name
    @@level = name
    @@hp = hp
    @@mp = mp
  end
  
  # def name
  #   self.@@name
  # end
  
  # def level
  #   self.@@level
  # end
end

# a = A.new("hiki", 17, 17, 17)
puts A.name