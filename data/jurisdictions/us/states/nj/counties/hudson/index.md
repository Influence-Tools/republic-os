---
type: Jurisdiction
title: "Hudson County, NJ"
classification: county
fips: "34017"
state: "NJ"
demographics:
  population: 718323
  population_under_18: 141994
  population_18_64: 485536
  population_65_plus: 90793
  median_household_income: 91795
  poverty_rate: 14.93
  homeownership_rate: 30.72
  unemployment_rate: 6.01
  median_home_value: 539700
  gini_index: 0.5046
  vacancy_rate: 6.63
  race_white: 231594
  race_black: 85703
  race_asian: 122062
  race_native: 7051
  hispanic: 292607
  bachelors_plus: 360526
districts:
  - to: "us/states/nj/districts/08"
    rel: in-district
    area_weight: 0.6775
  - to: "us/states/nj/districts/09"
    rel: in-district
    area_weight: 0.1398
  - to: "us/states/nj/districts/10"
    rel: in-district
    area_weight: 0.1043
  - to: "us/states/ny/districts/10"
    rel: in-district
    area_weight: 0.0138
  - to: "us/states/nj/districts/senate/31"
    rel: in-district
    area_weight: 0.4105
  - to: "us/states/nj/districts/senate/33"
    rel: in-district
    area_weight: 0.2629
  - to: "us/states/nj/districts/senate/32"
    rel: in-district
    area_weight: 0.1435
  - to: "us/states/nj/districts/senate/29"
    rel: in-district
    area_weight: 0.0234
  - to: "us/states/nj/districts/house/31"
    rel: in-district
    area_weight: 0.4105
  - to: "us/states/nj/districts/house/33"
    rel: in-district
    area_weight: 0.2629
  - to: "us/states/nj/districts/house/32"
    rel: in-district
    area_weight: 0.1435
  - to: "us/states/nj/districts/house/29"
    rel: in-district
    area_weight: 0.0234
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, nj]
timestamp: "2026-07-03"
---

# Hudson County, NJ

County jurisdiction — 4 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 718323 |
| Under 18 | 141994 |
| 18–64 | 485536 |
| 65+ | 90793 |
| Median household income | 91795 |
| Poverty rate | 14.93 |
| Homeownership rate | 30.72 |
| Unemployment rate | 6.01 |
| Median home value | 539700 |
| Gini index | 0.5046 |
| Vacancy rate | 6.63 |
| White | 231594 |
| Black | 85703 |
| Asian | 122062 |
| Native | 7051 |
| Hispanic/Latino | 292607 |
| Bachelor's or higher | 360526 |

## Districts

- [NJ-08](/us/states/nj/districts/08.md) — 68% (congressional)
- [NJ-09](/us/states/nj/districts/09.md) — 14% (congressional)
- [NJ-10](/us/states/nj/districts/10.md) — 10% (congressional)
- [NY-10](/us/states/ny/districts/10.md) — 1% (congressional)
- [NJ Senate District 31](/us/states/nj/districts/senate/31.md) — 41% (state senate)
- [NJ Senate District 33](/us/states/nj/districts/senate/33.md) — 26% (state senate)
- [NJ Senate District 32](/us/states/nj/districts/senate/32.md) — 14% (state senate)
- [NJ Senate District 29](/us/states/nj/districts/senate/29.md) — 2% (state senate)
- [NJ House District 31](/us/states/nj/districts/house/31.md) — 41% (state house)
- [NJ House District 33](/us/states/nj/districts/house/33.md) — 26% (state house)
- [NJ House District 32](/us/states/nj/districts/house/32.md) — 14% (state house)
- [NJ House District 29](/us/states/nj/districts/house/29.md) — 2% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
