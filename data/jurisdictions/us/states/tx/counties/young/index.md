---
type: Jurisdiction
title: "Young County, TX"
classification: county
fips: "48503"
state: "TX"
demographics:
  population: 18029
  population_under_18: 4146
  population_18_64: 10056
  population_65_plus: 3827
  median_household_income: 68010
  poverty_rate: 16.5
  homeownership_rate: 74.07
  unemployment_rate: 3.54
  median_home_value: 175800
  gini_index: 0.4532
  vacancy_rate: 10.56
  race_white: 14716
  race_black: 142
  race_asian: 194
  race_native: 47
  hispanic: 3692
  bachelors_plus: 3927
districts:
  - to: "us/states/tx/districts/25"
    rel: in-district
    area_weight: 0.9997
  - to: "us/states/tx/districts/senate/30"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/tx/districts/house/68"
    rel: in-district
    area_weight: 0.9998
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, tx]
timestamp: "2026-07-03"
---

# Young County, TX

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 18029 |
| Under 18 | 4146 |
| 18–64 | 10056 |
| 65+ | 3827 |
| Median household income | 68010 |
| Poverty rate | 16.5 |
| Homeownership rate | 74.07 |
| Unemployment rate | 3.54 |
| Median home value | 175800 |
| Gini index | 0.4532 |
| Vacancy rate | 10.56 |
| White | 14716 |
| Black | 142 |
| Asian | 194 |
| Native | 47 |
| Hispanic/Latino | 3692 |
| Bachelor's or higher | 3927 |

## Districts

- [TX-25](/us/states/tx/districts/25.md) — 100% (congressional)
- [TX Senate District 30](/us/states/tx/districts/senate/30.md) — 100% (state senate)
- [TX House District 68](/us/states/tx/districts/house/68.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
