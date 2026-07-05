---
type: Jurisdiction
title: "Piatt County, IL"
classification: county
fips: "17147"
state: "IL"
demographics:
  population: 16695
  population_under_18: 3608
  population_18_64: 9558
  population_65_plus: 3529
  median_household_income: 94811
  poverty_rate: 6.14
  homeownership_rate: 84.85
  unemployment_rate: 2.78
  median_home_value: 180600
  gini_index: 0.4071
  vacancy_rate: 6.58
  race_white: 15860
  race_black: 240
  race_asian: 106
  race_native: 14
  hispanic: 271
  bachelors_plus: 5352
districts:
  - to: "us/states/il/districts/15"
    rel: in-district
    area_weight: 0.5551
  - to: "us/states/il/districts/13"
    rel: in-district
    area_weight: 0.4448
  - to: "us/states/il/districts/senate/44"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/il/districts/house/88"
    rel: in-district
    area_weight: 1.0
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, il]
timestamp: "2026-07-03"
---

# Piatt County, IL

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 16695 |
| Under 18 | 3608 |
| 18–64 | 9558 |
| 65+ | 3529 |
| Median household income | 94811 |
| Poverty rate | 6.14 |
| Homeownership rate | 84.85 |
| Unemployment rate | 2.78 |
| Median home value | 180600 |
| Gini index | 0.4071 |
| Vacancy rate | 6.58 |
| White | 15860 |
| Black | 240 |
| Asian | 106 |
| Native | 14 |
| Hispanic/Latino | 271 |
| Bachelor's or higher | 5352 |

## Districts

- [IL-15](/us/states/il/districts/15.md) — 56% (congressional)
- [IL-13](/us/states/il/districts/13.md) — 44% (congressional)
- [IL Senate District 44](/us/states/il/districts/senate/44.md) — 100% (state senate)
- [IL House District 88](/us/states/il/districts/house/88.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
