---
type: Jurisdiction
title: "Calvert County, MD"
classification: county
fips: "24009"
state: "MD"
demographics:
  population: 94313
  population_under_18: 21796
  population_18_64: 57115
  population_65_plus: 15402
  median_household_income: 133922
  poverty_rate: 3.87
  homeownership_rate: 87.2
  unemployment_rate: 2.69
  median_home_value: 460200
  gini_index: 0.3825
  vacancy_rate: 7.35
  race_white: 70778
  race_black: 11502
  race_asian: 1837
  race_native: 225
  hispanic: 4863
  bachelors_plus: 34986
districts:
  - to: "us/states/md/districts/05"
    rel: in-district
    area_weight: 0.6894
  - to: "us/states/md/districts/senate/27"
    rel: in-district
    area_weight: 0.5895
  - to: "us/states/md/districts/senate/29"
    rel: in-district
    area_weight: 0.0993
  - to: "us/states/md/districts/house/27c"
    rel: in-district
    area_weight: 0.4653
  - to: "us/states/md/districts/house/27b"
    rel: in-district
    area_weight: 0.1242
  - to: "us/states/md/districts/house/29c"
    rel: in-district
    area_weight: 0.0992
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, md]
timestamp: "2026-07-03"
---

# Calvert County, MD

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 94313 |
| Under 18 | 21796 |
| 18–64 | 57115 |
| 65+ | 15402 |
| Median household income | 133922 |
| Poverty rate | 3.87 |
| Homeownership rate | 87.2 |
| Unemployment rate | 2.69 |
| Median home value | 460200 |
| Gini index | 0.3825 |
| Vacancy rate | 7.35 |
| White | 70778 |
| Black | 11502 |
| Asian | 1837 |
| Native | 225 |
| Hispanic/Latino | 4863 |
| Bachelor's or higher | 34986 |

## Districts

- [MD-05](/us/states/md/districts/05.md) — 69% (congressional)
- [MD Senate District 27](/us/states/md/districts/senate/27.md) — 59% (state senate)
- [MD Senate District 29](/us/states/md/districts/senate/29.md) — 10% (state senate)
- [MD House District 27C](/us/states/md/districts/house/27c.md) — 47% (state house)
- [MD House District 27B](/us/states/md/districts/house/27b.md) — 12% (state house)
- [MD House District 29C](/us/states/md/districts/house/29c.md) — 10% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
