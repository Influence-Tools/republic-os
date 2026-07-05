---
type: Jurisdiction
title: "Nash County, NC"
classification: county
fips: "37127"
state: "NC"
demographics:
  population: 96216
  population_under_18: 21210
  population_18_64: 56383
  population_65_plus: 18623
  median_household_income: 62426
  poverty_rate: 11.84
  homeownership_rate: 63.56
  unemployment_rate: 4.95
  median_home_value: 191000
  gini_index: 0.4523
  vacancy_rate: 11.42
  race_white: 46014
  race_black: 38655
  race_asian: 1034
  race_native: 620
  hispanic: 7925
  bachelors_plus: 19714
districts:
  - to: "us/states/nc/districts/01"
    rel: in-district
    area_weight: 0.9988
  - to: "us/states/nc/districts/senate/11"
    rel: in-district
    area_weight: 0.9997
  - to: "us/states/nc/districts/house/25"
    rel: in-district
    area_weight: 0.9647
  - to: "us/states/nc/districts/house/24"
    rel: in-district
    area_weight: 0.0349
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, nc]
timestamp: "2026-07-03"
---

# Nash County, NC

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 96216 |
| Under 18 | 21210 |
| 18–64 | 56383 |
| 65+ | 18623 |
| Median household income | 62426 |
| Poverty rate | 11.84 |
| Homeownership rate | 63.56 |
| Unemployment rate | 4.95 |
| Median home value | 191000 |
| Gini index | 0.4523 |
| Vacancy rate | 11.42 |
| White | 46014 |
| Black | 38655 |
| Asian | 1034 |
| Native | 620 |
| Hispanic/Latino | 7925 |
| Bachelor's or higher | 19714 |

## Districts

- [NC-01](/us/states/nc/districts/01.md) — 100% (congressional)
- [NC Senate District 11](/us/states/nc/districts/senate/11.md) — 100% (state senate)
- [NC House District 25](/us/states/nc/districts/house/25.md) — 96% (state house)
- [NC House District 24](/us/states/nc/districts/house/24.md) — 3% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
