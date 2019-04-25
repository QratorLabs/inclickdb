ATTACH TABLE graphite_series_reverse
(
    Date Date, 
    Level UInt32, 
    Path String, 
    Deleted UInt8, 
    Version UInt32
)
ENGINE = ReplacingMergeTree(Date, (Level, Path, Date), 1024, Version)
