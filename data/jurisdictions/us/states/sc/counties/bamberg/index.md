---
type: Jurisdiction
title: "Bamberg County, SC"
classification: county
fips: "45009"
state: "SC"
demographics:
  population: 13042
  population_under_18: 2382
  population_18_64: 7543
  population_65_plus: 3117
  median_household_income: 44370
  poverty_rate: 24.3
  homeownership_rate: 70.39
  unemployment_rate: 14.98
  median_home_value: 97800
  gini_index: 0.4751
  vacancy_rate: 29.43
  race_white: 4912
  race_black: 7763
  race_asian: 66
  race_native: 41
  hispanic: 183
  bachelors_plus: 2280
districts:
  - to: "us/states/sc/districts/06"
    rel: in-district
    area_weight: 0.9967
  - to: "us/states/sc/districts/senate/40"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/sc/districts/house/90"
    rel: in-district
    area_weight: 0.9994
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, sc]
timestamp: "2026-07-03"
---

# Bamberg County, SC

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 13042 |
| Under 18 | 2382 |
| 18–64 | 7543 |
| 65+ | 3117 |
| Median household income | 44370 |
| Poverty rate | 24.3 |
| Homeownership rate | 70.39 |
| Unemployment rate | 14.98 |
| Median home value | 97800 |
| Gini index | 0.4751 |
| Vacancy rate | 29.43 |
| White | 4912 |
| Black | 7763 |
| Asian | 66 |
| Native | 41 |
| Hispanic/Latino | 183 |
| Bachelor's or higher | 2280 |

## Districts

- [SC-06](/us/states/sc/districts/06.md) — 100% (congressional)
- [SC Senate District 40](/us/states/sc/districts/senate/40.md) — 100% (state senate)
- [SC House District 90](/us/states/sc/districts/house/90.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
