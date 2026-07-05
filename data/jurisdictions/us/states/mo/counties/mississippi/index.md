---
type: Jurisdiction
title: "Mississippi County, MO"
classification: county
fips: "29133"
state: "MO"
demographics:
  population: 11902
  population_under_18: 2688
  population_18_64: 6970
  population_65_plus: 2244
  median_household_income: 48160
  poverty_rate: 19.04
  homeownership_rate: 62.94
  unemployment_rate: 2.74
  median_home_value: 109000
  gini_index: 0.432
  vacancy_rate: 14.98
  race_white: 8467
  race_black: 2257
  race_asian: 76
  race_native: 4
  hispanic: 96
  bachelors_plus: 1580
districts:
  - to: "us/states/mo/districts/08"
    rel: in-district
    area_weight: 0.9996
  - to: "us/states/mo/districts/senate/25"
    rel: in-district
    area_weight: 0.9996
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, mo]
timestamp: "2026-07-03"
---

# Mississippi County, MO

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 11902 |
| Under 18 | 2688 |
| 18–64 | 6970 |
| 65+ | 2244 |
| Median household income | 48160 |
| Poverty rate | 19.04 |
| Homeownership rate | 62.94 |
| Unemployment rate | 2.74 |
| Median home value | 109000 |
| Gini index | 0.432 |
| Vacancy rate | 14.98 |
| White | 8467 |
| Black | 2257 |
| Asian | 76 |
| Native | 4 |
| Hispanic/Latino | 96 |
| Bachelor's or higher | 1580 |

## Districts

- [MO-08](/us/states/mo/districts/08.md) — 100% (congressional)
- [MO Senate District 25](/us/states/mo/districts/senate/25.md) — 100% (state senate)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
