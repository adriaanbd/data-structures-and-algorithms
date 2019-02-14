class MyNode
  attr_reader :key # read
  attr_accessor :next_pointer # read / write

  def initialize(key)
    @key = key
    @next_pointer = nil
  end
end