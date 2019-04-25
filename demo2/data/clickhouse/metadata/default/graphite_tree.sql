ATTACH TABLE graphite_tree
(
    Date Date, 
    Level UInt32, 
    Path String, 
    Deleted UInt8, 
    Version UInt32
)
ENGINE = ReplacingMergeTree(Date, (Level, Path), 1024, Version)
