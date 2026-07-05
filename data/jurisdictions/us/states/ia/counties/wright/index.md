---
type: Jurisdiction
title: "Wright County, IA"
classification: county
fips: "19197"
state: "IA"
demographics:
  population: 12791
  population_under_18: 3329
  population_18_64: 6635
  population_65_plus: 2827
  median_household_income: 67190
  poverty_rate: 16.75
  homeownership_rate: 77.0
  unemployment_rate: 1.84
  median_home_value: 119600
  gini_index: 0.4667
  vacancy_rate: 14.73
  race_white: 9848
  race_black: 56
  race_asian: 60
  race_native: 70
  hispanic: 2547
  bachelors_plus: 2690
districts:
  - to: "us/states/ia/districts/04"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/ia/districts/senate/28"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/ia/districts/house/56"
    rel: in-district
    area_weight: 0.6922
  - to: "us/states/ia/districts/house/55"
    rel: in-district
    area_weight: 0.3078
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ia]
timestamp: "2026-07-03"
---

# Wright County, IA

County jurisdiction — 3 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 12791 |
| Under 18 | 3329 |
| 18–64 | 6635 |
| 65+ | 2827 |
| Median household income | 67190 |
| Poverty rate | 16.75 |
| Homeownership rate | 77.0 |
| Unemployment rate | 1.84 |
| Median home value | 119600 |
| Gini index | 0.4667 |
| Vacancy rate | 14.73 |
| White | 9848 |
| Black | 56 |
| Asian | 60 |
| Native | 70 |
| Hispanic/Latino | 2547 |
| Bachelor's or higher | 2690 |

## Districts

- [IA-04](/us/states/ia/districts/04.md) — 100% (congressional)
- [IA Senate District 28](/us/states/ia/districts/senate/28.md) — 100% (state senate)
- [IA House District 56](/us/states/ia/districts/house/56.md) — 69% (state house)
- [IA House District 55](/us/states/ia/districts/house/55.md) — 31% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
