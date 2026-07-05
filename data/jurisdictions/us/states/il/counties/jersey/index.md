---
type: Jurisdiction
title: "Jersey County, IL"
classification: county
fips: "17083"
state: "IL"
demographics:
  population: 21274
  population_under_18: 4207
  population_18_64: 12676
  population_65_plus: 4391
  median_household_income: 80361
  poverty_rate: 8.83
  homeownership_rate: 80.54
  unemployment_rate: 3.4
  median_home_value: 171900
  gini_index: 0.4248
  vacancy_rate: 20.01
  race_white: 20197
  race_black: 118
  race_asian: 143
  race_native: 5
  hispanic: 340
  bachelors_plus: 4562
districts:
  - to: "us/states/il/districts/15"
    rel: in-district
    area_weight: 0.9997
  - to: "us/states/il/districts/senate/50"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/il/districts/house/100"
    rel: in-district
    area_weight: 0.9999
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, il]
timestamp: "2026-07-03"
---

# Jersey County, IL

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 21274 |
| Under 18 | 4207 |
| 18–64 | 12676 |
| 65+ | 4391 |
| Median household income | 80361 |
| Poverty rate | 8.83 |
| Homeownership rate | 80.54 |
| Unemployment rate | 3.4 |
| Median home value | 171900 |
| Gini index | 0.4248 |
| Vacancy rate | 20.01 |
| White | 20197 |
| Black | 118 |
| Asian | 143 |
| Native | 5 |
| Hispanic/Latino | 340 |
| Bachelor's or higher | 4562 |

## Districts

- [IL-15](/us/states/il/districts/15.md) — 100% (congressional)
- [IL Senate District 50](/us/states/il/districts/senate/50.md) — 100% (state senate)
- [IL House District 100](/us/states/il/districts/house/100.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
