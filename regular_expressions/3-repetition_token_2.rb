#!/usr/bin/env ruby
puts ARGV[0].scan(/\bh?[bt]{1,4}n\b/).join("\n")