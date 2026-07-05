---
type: Jurisdiction
title: "Brazoria County, TX"
classification: county
fips: "48039"
state: "TX"
demographics:
  population: 391255
  population_under_18: 100070
  population_18_64: 240961
  population_65_plus: 50224
  median_household_income: 97993
  poverty_rate: 7.39
  homeownership_rate: 74.14
  unemployment_rate: 4.68
  median_home_value: 301600
  gini_index: 0.4187
  vacancy_rate: 10.93
  race_white: 186775
  race_black: 63338
  race_asian: 29076
  race_native: 1831
  hispanic: 123657
  bachelors_plus: 118545
districts:
  - to: "us/states/tx/districts/14"
    rel: in-district
    area_weight: 0.7478
  - to: "us/states/tx/districts/22"
    rel: in-district
    area_weight: 0.1414
  - to: "us/states/tx/districts/09"
    rel: in-district
    area_weight: 0.0191
  - to: "us/states/tx/districts/senate/17"
    rel: in-district
    area_weight: 0.6728
  - to: "us/states/tx/districts/senate/11"
    rel: in-district
    area_weight: 0.2334
  - to: "us/states/tx/districts/house/25"
    rel: in-district
    area_weight: 0.5832
  - to: "us/states/tx/districts/house/29"
    rel: in-district
    area_weight: 0.3228
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, tx]
timestamp: "2026-07-03"
---

# Brazoria County, TX

County jurisdiction — 6 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 391255 |
| Under 18 | 100070 |
| 18–64 | 240961 |
| 65+ | 50224 |
| Median household income | 97993 |
| Poverty rate | 7.39 |
| Homeownership rate | 74.14 |
| Unemployment rate | 4.68 |
| Median home value | 301600 |
| Gini index | 0.4187 |
| Vacancy rate | 10.93 |
| White | 186775 |
| Black | 63338 |
| Asian | 29076 |
| Native | 1831 |
| Hispanic/Latino | 123657 |
| Bachelor's or higher | 118545 |

## Districts

- [TX-14](/us/states/tx/districts/14.md) — 75% (congressional)
- [TX-22](/us/states/tx/districts/22.md) — 14% (congressional)
- [TX-09](/us/states/tx/districts/09.md) — 2% (congressional)
- [TX Senate District 17](/us/states/tx/districts/senate/17.md) — 67% (state senate)
- [TX Senate District 11](/us/states/tx/districts/senate/11.md) — 23% (state senate)
- [TX House District 25](/us/states/tx/districts/house/25.md) — 58% (state house)
- [TX House District 29](/us/states/tx/districts/house/29.md) — 32% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
