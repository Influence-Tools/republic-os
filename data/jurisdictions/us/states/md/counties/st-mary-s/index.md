---
type: Jurisdiction
title: "St. Mary's County, MD"
classification: county
fips: "24037"
state: "MD"
demographics:
  population: 115126
  population_under_18: 27549
  population_18_64: 71433
  population_65_plus: 16144
  median_household_income: 119446
  poverty_rate: 7.98
  homeownership_rate: 73.17
  unemployment_rate: 3.56
  median_home_value: 407600
  gini_index: 0.4087
  vacancy_rate: 8.51
  race_white: 82070
  race_black: 16847
  race_asian: 3062
  race_native: 130
  hispanic: 7072
  bachelors_plus: 40882
districts:
  - to: "us/states/md/districts/05"
    rel: in-district
    area_weight: 0.5304
  - to: "us/states/md/districts/senate/29"
    rel: in-district
    area_weight: 0.5266
  - to: "us/states/md/districts/house/29a"
    rel: in-district
    area_weight: 0.2804
  - to: "us/states/md/districts/house/29c"
    rel: in-district
    area_weight: 0.1296
  - to: "us/states/md/districts/house/29b"
    rel: in-district
    area_weight: 0.1166
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, md]
timestamp: "2026-07-03"
---

# St. Mary's County, MD

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 115126 |
| Under 18 | 27549 |
| 18–64 | 71433 |
| 65+ | 16144 |
| Median household income | 119446 |
| Poverty rate | 7.98 |
| Homeownership rate | 73.17 |
| Unemployment rate | 3.56 |
| Median home value | 407600 |
| Gini index | 0.4087 |
| Vacancy rate | 8.51 |
| White | 82070 |
| Black | 16847 |
| Asian | 3062 |
| Native | 130 |
| Hispanic/Latino | 7072 |
| Bachelor's or higher | 40882 |

## Districts

- [MD-05](/us/states/md/districts/05.md) — 53% (congressional)
- [MD Senate District 29](/us/states/md/districts/senate/29.md) — 53% (state senate)
- [MD House District 29A](/us/states/md/districts/house/29a.md) — 28% (state house)
- [MD House District 29C](/us/states/md/districts/house/29c.md) — 13% (state house)
- [MD House District 29B](/us/states/md/districts/house/29b.md) — 12% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
