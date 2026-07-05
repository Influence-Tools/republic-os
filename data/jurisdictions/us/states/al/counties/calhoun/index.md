---
type: Jurisdiction
title: "Calhoun County, AL"
classification: county
fips: "01015"
state: "AL"
demographics:
  population: 116090
  population_under_18: 24893
  population_18_64: 70041
  population_65_plus: 21156
  median_household_income: 55029
  poverty_rate: 17.89
  homeownership_rate: 70.32
  unemployment_rate: 5.97
  median_home_value: 156600
  gini_index: 0.4571
  vacancy_rate: 15.64
  race_white: 81706
  race_black: 25450
  race_asian: 986
  race_native: 450
  hispanic: 5388
  bachelors_plus: 22540
districts:
  - to: "us/states/al/districts/03"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/al/districts/senate/12"
    rel: in-district
    area_weight: 0.9997
  - to: "us/states/al/districts/house/29"
    rel: in-district
    area_weight: 0.3669
  - to: "us/states/al/districts/house/40"
    rel: in-district
    area_weight: 0.2749
  - to: "us/states/al/districts/house/36"
    rel: in-district
    area_weight: 0.1906
  - to: "us/states/al/districts/house/32"
    rel: in-district
    area_weight: 0.1181
  - to: "us/states/al/districts/house/35"
    rel: in-district
    area_weight: 0.0495
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, al]
timestamp: "2026-07-03"
---

# Calhoun County, AL

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 116090 |
| Under 18 | 24893 |
| 18–64 | 70041 |
| 65+ | 21156 |
| Median household income | 55029 |
| Poverty rate | 17.89 |
| Homeownership rate | 70.32 |
| Unemployment rate | 5.97 |
| Median home value | 156600 |
| Gini index | 0.4571 |
| Vacancy rate | 15.64 |
| White | 81706 |
| Black | 25450 |
| Asian | 986 |
| Native | 450 |
| Hispanic/Latino | 5388 |
| Bachelor's or higher | 22540 |

## Districts

- [AL-03](/us/states/al/districts/03.md) — 100% (congressional)
- [AL Senate District 12](/us/states/al/districts/senate/12.md) — 100% (state senate)
- [AL House District 29](/us/states/al/districts/house/29.md) — 37% (state house)
- [AL House District 40](/us/states/al/districts/house/40.md) — 27% (state house)
- [AL House District 36](/us/states/al/districts/house/36.md) — 19% (state house)
- [AL House District 32](/us/states/al/districts/house/32.md) — 12% (state house)
- [AL House District 35](/us/states/al/districts/house/35.md) — 5% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
