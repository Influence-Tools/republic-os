---
type: Jurisdiction
title: "Garrett County, MD"
classification: county
fips: "24023"
state: "MD"
demographics:
  population: 28615
  population_under_18: 5075
  population_18_64: 16615
  population_65_plus: 6925
  median_household_income: 67688
  poverty_rate: 11.25
  homeownership_rate: 79.72
  unemployment_rate: 4.35
  median_home_value: 235300
  gini_index: 0.4929
  vacancy_rate: 32.53
  race_white: 27216
  race_black: 175
  race_asian: 137
  race_native: 68
  hispanic: 393
  bachelors_plus: 8230
districts:
  - to: "us/states/md/districts/06"
    rel: in-district
    area_weight: 0.9982
  - to: "us/states/md/districts/senate/1"
    rel: in-district
    area_weight: 0.9993
  - to: "us/states/md/districts/house/1a"
    rel: in-district
    area_weight: 0.9993
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, md]
timestamp: "2026-07-03"
---

# Garrett County, MD

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 28615 |
| Under 18 | 5075 |
| 18–64 | 16615 |
| 65+ | 6925 |
| Median household income | 67688 |
| Poverty rate | 11.25 |
| Homeownership rate | 79.72 |
| Unemployment rate | 4.35 |
| Median home value | 235300 |
| Gini index | 0.4929 |
| Vacancy rate | 32.53 |
| White | 27216 |
| Black | 175 |
| Asian | 137 |
| Native | 68 |
| Hispanic/Latino | 393 |
| Bachelor's or higher | 8230 |

## Districts

- [MD-06](/us/states/md/districts/06.md) — 100% (congressional)
- [MD Senate District 1](/us/states/md/districts/senate/1.md) — 100% (state senate)
- [MD House District 1A](/us/states/md/districts/house/1a.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
