---
type: Jurisdiction
title: "Steuben County, NY"
classification: county
fips: "36101"
state: "NY"
demographics:
  population: 92588
  population_under_18: 19920
  population_18_64: 53406
  population_65_plus: 19262
  median_household_income: 65887
  poverty_rate: 13.78
  homeownership_rate: 73.28
  unemployment_rate: 5.97
  median_home_value: 137900
  gini_index: 0.4516
  vacancy_rate: 17.72
  race_white: 85025
  race_black: 1522
  race_asian: 1546
  race_native: 75
  hispanic: 1855
  bachelors_plus: 25686
districts:
  - to: "us/states/ny/districts/23"
    rel: in-district
    area_weight: 0.7752
  - to: "us/states/ny/districts/24"
    rel: in-district
    area_weight: 0.2247
  - to: "us/states/ny/districts/senate/58"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/ny/districts/house/132"
    rel: in-district
    area_weight: 0.5974
  - to: "us/states/ny/districts/house/148"
    rel: in-district
    area_weight: 0.2039
  - to: "us/states/ny/districts/house/133"
    rel: in-district
    area_weight: 0.1987
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ny]
timestamp: "2026-07-03"
---

# Steuben County, NY

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 92588 |
| Under 18 | 19920 |
| 18–64 | 53406 |
| 65+ | 19262 |
| Median household income | 65887 |
| Poverty rate | 13.78 |
| Homeownership rate | 73.28 |
| Unemployment rate | 5.97 |
| Median home value | 137900 |
| Gini index | 0.4516 |
| Vacancy rate | 17.72 |
| White | 85025 |
| Black | 1522 |
| Asian | 1546 |
| Native | 75 |
| Hispanic/Latino | 1855 |
| Bachelor's or higher | 25686 |

## Districts

- [NY-23](/us/states/ny/districts/23.md) — 78% (congressional)
- [NY-24](/us/states/ny/districts/24.md) — 22% (congressional)
- [NY Senate District 58](/us/states/ny/districts/senate/58.md) — 100% (state senate)
- [NY House District 132](/us/states/ny/districts/house/132.md) — 60% (state house)
- [NY House District 148](/us/states/ny/districts/house/148.md) — 20% (state house)
- [NY House District 133](/us/states/ny/districts/house/133.md) — 20% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
