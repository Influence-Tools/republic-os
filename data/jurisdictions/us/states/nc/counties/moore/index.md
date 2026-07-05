---
type: Jurisdiction
title: "Moore County, NC"
classification: county
fips: "37125"
state: "NC"
demographics:
  population: 104876
  population_under_18: 22803
  population_18_64: 56842
  population_65_plus: 25231
  median_household_income: 86080
  poverty_rate: 10.07
  homeownership_rate: 76.39
  unemployment_rate: 4.84
  median_home_value: 351400
  gini_index: 0.4485
  vacancy_rate: 12.46
  race_white: 81108
  race_black: 9406
  race_asian: 1322
  race_native: 474
  hispanic: 8196
  bachelors_plus: 44451
districts:
  - to: "us/states/nc/districts/09"
    rel: in-district
    area_weight: 0.9954
  - to: "us/states/nc/districts/senate/21"
    rel: in-district
    area_weight: 0.9996
  - to: "us/states/nc/districts/house/78"
    rel: in-district
    area_weight: 0.4711
  - to: "us/states/nc/districts/house/51"
    rel: in-district
    area_weight: 0.3284
  - to: "us/states/nc/districts/house/52"
    rel: in-district
    area_weight: 0.2003
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, nc]
timestamp: "2026-07-03"
---

# Moore County, NC

County jurisdiction — 2 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 104876 |
| Under 18 | 22803 |
| 18–64 | 56842 |
| 65+ | 25231 |
| Median household income | 86080 |
| Poverty rate | 10.07 |
| Homeownership rate | 76.39 |
| Unemployment rate | 4.84 |
| Median home value | 351400 |
| Gini index | 0.4485 |
| Vacancy rate | 12.46 |
| White | 81108 |
| Black | 9406 |
| Asian | 1322 |
| Native | 474 |
| Hispanic/Latino | 8196 |
| Bachelor's or higher | 44451 |

## Districts

- [NC-09](/us/states/nc/districts/09.md) — 100% (congressional)
- [NC Senate District 21](/us/states/nc/districts/senate/21.md) — 100% (state senate)
- [NC House District 78](/us/states/nc/districts/house/78.md) — 47% (state house)
- [NC House District 51](/us/states/nc/districts/house/51.md) — 33% (state house)
- [NC House District 52](/us/states/nc/districts/house/52.md) — 20% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
