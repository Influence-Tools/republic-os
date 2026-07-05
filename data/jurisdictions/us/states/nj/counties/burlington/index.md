---
type: Jurisdiction
title: "Burlington County, NJ"
classification: county
fips: "34005"
state: "NJ"
demographics:
  population: 467805
  population_under_18: 96126
  population_18_64: 285974
  population_65_plus: 85705
  median_household_income: 108111
  poverty_rate: 6.65
  homeownership_rate: 76.13
  unemployment_rate: 5.27
  median_home_value: 354000
  gini_index: 0.4292
  vacancy_rate: 4.88
  race_white: 301052
  race_black: 76226
  race_asian: 27207
  race_native: 956
  hispanic: 44974
  bachelors_plus: 194840
districts:
  - to: "us/states/nj/districts/03"
    rel: in-district
    area_weight: 0.9892
  - to: "us/states/nj/districts/01"
    rel: in-district
    area_weight: 0.0081
  - to: "us/states/nj/districts/senate/8"
    rel: in-district
    area_weight: 0.8378
  - to: "us/states/nj/districts/senate/7"
    rel: in-district
    area_weight: 0.1355
  - to: "us/states/nj/districts/senate/12"
    rel: in-district
    area_weight: 0.0214
  - to: "us/states/nj/districts/house/8"
    rel: in-district
    area_weight: 0.8378
  - to: "us/states/nj/districts/house/7"
    rel: in-district
    area_weight: 0.1355
  - to: "us/states/nj/districts/house/12"
    rel: in-district
    area_weight: 0.0214
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, nj]
timestamp: "2026-07-03"
---

# Burlington County, NJ

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 467805 |
| Under 18 | 96126 |
| 18–64 | 285974 |
| 65+ | 85705 |
| Median household income | 108111 |
| Poverty rate | 6.65 |
| Homeownership rate | 76.13 |
| Unemployment rate | 5.27 |
| Median home value | 354000 |
| Gini index | 0.4292 |
| Vacancy rate | 4.88 |
| White | 301052 |
| Black | 76226 |
| Asian | 27207 |
| Native | 956 |
| Hispanic/Latino | 44974 |
| Bachelor's or higher | 194840 |

## Districts

- [NJ-03](/us/states/nj/districts/03.md) — 99% (congressional)
- [NJ-01](/us/states/nj/districts/01.md) — 1% (congressional)
- [NJ Senate District 8](/us/states/nj/districts/senate/8.md) — 84% (state senate)
- [NJ Senate District 7](/us/states/nj/districts/senate/7.md) — 14% (state senate)
- [NJ Senate District 12](/us/states/nj/districts/senate/12.md) — 2% (state senate)
- [NJ House District 8](/us/states/nj/districts/house/8.md) — 84% (state house)
- [NJ House District 7](/us/states/nj/districts/house/7.md) — 14% (state house)
- [NJ House District 12](/us/states/nj/districts/house/12.md) — 2% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
