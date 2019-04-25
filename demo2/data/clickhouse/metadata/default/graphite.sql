ATTACH TABLE graphite
(
    Path String, 
    Value Float64, 
    Time UInt32, 
    Date Date, 
    Timestamp UInt32
)
ENGINE = GraphiteMergeTree(Date, (Path, Time), 8192, 'graphite_rollup')
