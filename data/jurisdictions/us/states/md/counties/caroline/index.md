---
type: Jurisdiction
title: "Caroline County, MD"
classification: county
fips: "24011"
state: "MD"
demographics:
  population: 33669
  population_under_18: 8056
  population_18_64: 19782
  population_65_plus: 5831
  median_household_income: 68457
  poverty_rate: 12.16
  homeownership_rate: 71.85
  unemployment_rate: 5.69
  median_home_value: 290100
  gini_index: 0.4253
  vacancy_rate: 7.66
  race_white: 24605
  race_black: 4340
  race_asian: 251
  race_native: 358
  hispanic: 3122
  bachelors_plus: 5276
districts:
  - to: "us/states/md/districts/01"
    rel: in-district
    area_weight: 0.9993
  - to: "us/states/md/districts/senate/37"
    rel: in-district
    area_weight: 0.6479
  - to: "us/states/md/districts/senate/36"
    rel: in-district
    area_weight: 0.352
  - to: "us/states/md/districts/house/37b"
    rel: in-district
    area_weight: 0.6479
  - to: "us/states/md/districts/house/36"
    rel: in-district
    area_weight: 0.352
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, md]
timestamp: "2026-07-03"
---

# Caroline County, MD

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 33669 |
| Under 18 | 8056 |
| 18–64 | 19782 |
| 65+ | 5831 |
| Median household income | 68457 |
| Poverty rate | 12.16 |
| Homeownership rate | 71.85 |
| Unemployment rate | 5.69 |
| Median home value | 290100 |
| Gini index | 0.4253 |
| Vacancy rate | 7.66 |
| White | 24605 |
| Black | 4340 |
| Asian | 251 |
| Native | 358 |
| Hispanic/Latino | 3122 |
| Bachelor's or higher | 5276 |

## Districts

- [MD-01](/us/states/md/districts/01.md) — 100% (congressional)
- [MD Senate District 37](/us/states/md/districts/senate/37.md) — 65% (state senate)
- [MD Senate District 36](/us/states/md/districts/senate/36.md) — 35% (state senate)
- [MD House District 37B](/us/states/md/districts/house/37b.md) — 65% (state house)
- [MD House District 36](/us/states/md/districts/house/36.md) — 35% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
