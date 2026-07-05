---
type: Jurisdiction
title: "Chemung County, NY"
classification: county
fips: "36015"
state: "NY"
demographics:
  population: 82147
  population_under_18: 17169
  population_18_64: 48285
  population_65_plus: 16693
  median_household_income: 63716
  poverty_rate: 16.31
  homeownership_rate: 68.44
  unemployment_rate: 6.15
  median_home_value: 141100
  gini_index: 0.4655
  vacancy_rate: 10.17
  race_white: 69816
  race_black: 5355
  race_asian: 1271
  race_native: 261
  hispanic: 3085
  bachelors_plus: 22937
districts:
  - to: "us/states/ny/districts/23"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/ny/districts/senate/58"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/ny/districts/house/124"
    rel: in-district
    area_weight: 0.6037
  - to: "us/states/ny/districts/house/132"
    rel: in-district
    area_weight: 0.3961
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ny]
timestamp: "2026-07-03"
---

# Chemung County, NY

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 82147 |
| Under 18 | 17169 |
| 18–64 | 48285 |
| 65+ | 16693 |
| Median household income | 63716 |
| Poverty rate | 16.31 |
| Homeownership rate | 68.44 |
| Unemployment rate | 6.15 |
| Median home value | 141100 |
| Gini index | 0.4655 |
| Vacancy rate | 10.17 |
| White | 69816 |
| Black | 5355 |
| Asian | 1271 |
| Native | 261 |
| Hispanic/Latino | 3085 |
| Bachelor's or higher | 22937 |

## Districts

- [NY-23](/us/states/ny/districts/23.md) — 100% (congressional)
- [NY Senate District 58](/us/states/ny/districts/senate/58.md) — 100% (state senate)
- [NY House District 124](/us/states/ny/districts/house/124.md) — 60% (state house)
- [NY House District 132](/us/states/ny/districts/house/132.md) — 40% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
