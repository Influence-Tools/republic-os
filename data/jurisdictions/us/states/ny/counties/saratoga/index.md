---
type: Jurisdiction
title: "Saratoga County, NY"
classification: county
fips: "36091"
state: "NY"
demographics:
  population: 238284
  population_under_18: 45523
  population_18_64: 145177
  population_65_plus: 47584
  median_household_income: 100787
  poverty_rate: 7.06
  homeownership_rate: 72.3
  unemployment_rate: 3.27
  median_home_value: 348600
  gini_index: 0.4459
  vacancy_rate: 9.1
  race_white: 209586
  race_black: 4078
  race_asian: 7114
  race_native: 467
  hispanic: 9412
  bachelors_plus: 114695
districts:
  - to: "us/states/ny/districts/21"
    rel: in-district
    area_weight: 0.5792
  - to: "us/states/ny/districts/20"
    rel: in-district
    area_weight: 0.4208
  - to: "us/states/ny/districts/senate/44"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/ny/districts/house/114"
    rel: in-district
    area_weight: 0.3604
  - to: "us/states/ny/districts/house/112"
    rel: in-district
    area_weight: 0.3227
  - to: "us/states/ny/districts/house/113"
    rel: in-district
    area_weight: 0.3081
  - to: "us/states/ny/districts/house/108"
    rel: in-district
    area_weight: 0.0087
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ny]
timestamp: "2026-07-03"
---

# Saratoga County, NY

County jurisdiction — 2 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 238284 |
| Under 18 | 45523 |
| 18–64 | 145177 |
| 65+ | 47584 |
| Median household income | 100787 |
| Poverty rate | 7.06 |
| Homeownership rate | 72.3 |
| Unemployment rate | 3.27 |
| Median home value | 348600 |
| Gini index | 0.4459 |
| Vacancy rate | 9.1 |
| White | 209586 |
| Black | 4078 |
| Asian | 7114 |
| Native | 467 |
| Hispanic/Latino | 9412 |
| Bachelor's or higher | 114695 |

## Districts

- [NY-21](/us/states/ny/districts/21.md) — 58% (congressional)
- [NY-20](/us/states/ny/districts/20.md) — 42% (congressional)
- [NY Senate District 44](/us/states/ny/districts/senate/44.md) — 100% (state senate)
- [NY House District 114](/us/states/ny/districts/house/114.md) — 36% (state house)
- [NY House District 112](/us/states/ny/districts/house/112.md) — 32% (state house)
- [NY House District 113](/us/states/ny/districts/house/113.md) — 31% (state house)
- [NY House District 108](/us/states/ny/districts/house/108.md) — 1% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
