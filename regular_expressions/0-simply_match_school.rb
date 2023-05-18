#!/usr/bin/env ruby
input = ARGV[0]
pattern = /School/
if input.match(pattern)
  puts "Input matches the pattern!"
else
  puts "Input does not match the pattern."
end
