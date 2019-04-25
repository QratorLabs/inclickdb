ATTACH TABLE graphite_tagged
(
    Date Date, 
    Tag1 String, 
    Path String, 
    Tags Array(String), 
    Version UInt32, 
    Deleted UInt8
)
ENGINE = ReplacingMergeTree(Date, (Tag1, Path, Date), 1024, Version)
