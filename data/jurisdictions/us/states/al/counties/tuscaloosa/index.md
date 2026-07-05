---
type: Jurisdiction
title: "Tuscaloosa County, AL"
classification: county
fips: "01125"
state: "AL"
demographics:
  population: 241212
  population_under_18: 66714
  population_18_64: 89122
  population_65_plus: 85376
  median_household_income: 68404
  poverty_rate: 15.62
  homeownership_rate: 61.42
  unemployment_rate: 6.61
  median_home_value: 260600
  gini_index: 0.4528
  vacancy_rate: 11.17
  race_white: 142491
  race_black: 75540
  race_asian: 4344
  race_native: 190
  hispanic: 14030
  bachelors_plus: 73504
districts:
  - to: "us/states/al/districts/04"
    rel: in-district
    area_weight: 0.6246
  - to: "us/states/al/districts/07"
    rel: in-district
    area_weight: 0.3752
  - to: "us/states/al/districts/senate/5"
    rel: in-district
    area_weight: 0.4837
  - to: "us/states/al/districts/senate/21"
    rel: in-district
    area_weight: 0.3456
  - to: "us/states/al/districts/senate/24"
    rel: in-district
    area_weight: 0.1705
  - to: "us/states/al/districts/house/16"
    rel: in-district
    area_weight: 0.3765
  - to: "us/states/al/districts/house/62"
    rel: in-district
    area_weight: 0.2387
  - to: "us/states/al/districts/house/61"
    rel: in-district
    area_weight: 0.165
  - to: "us/states/al/districts/house/72"
    rel: in-district
    area_weight: 0.096
  - to: "us/states/al/districts/house/71"
    rel: in-district
    area_weight: 0.0856
  - to: "us/states/al/districts/house/63"
    rel: in-district
    area_weight: 0.0192
  - to: "us/states/al/districts/house/70"
    rel: in-district
    area_weight: 0.0191
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, al]
timestamp: "2026-07-03"
---

# Tuscaloosa County, AL

County jurisdiction — 2 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 241212 |
| Under 18 | 66714 |
| 18–64 | 89122 |
| 65+ | 85376 |
| Median household income | 68404 |
| Poverty rate | 15.62 |
| Homeownership rate | 61.42 |
| Unemployment rate | 6.61 |
| Median home value | 260600 |
| Gini index | 0.4528 |
| Vacancy rate | 11.17 |
| White | 142491 |
| Black | 75540 |
| Asian | 4344 |
| Native | 190 |
| Hispanic/Latino | 14030 |
| Bachelor's or higher | 73504 |

## Districts

- [AL-04](/us/states/al/districts/04.md) — 62% (congressional)
- [AL-07](/us/states/al/districts/07.md) — 38% (congressional)
- [AL Senate District 5](/us/states/al/districts/senate/5.md) — 48% (state senate)
- [AL Senate District 21](/us/states/al/districts/senate/21.md) — 35% (state senate)
- [AL Senate District 24](/us/states/al/districts/senate/24.md) — 17% (state senate)
- [AL House District 16](/us/states/al/districts/house/16.md) — 38% (state house)
- [AL House District 62](/us/states/al/districts/house/62.md) — 24% (state house)
- [AL House District 61](/us/states/al/districts/house/61.md) — 16% (state house)
- [AL House District 72](/us/states/al/districts/house/72.md) — 10% (state house)
- [AL House District 71](/us/states/al/districts/house/71.md) — 9% (state house)
- [AL House District 63](/us/states/al/districts/house/63.md) — 2% (state house)
- [AL House District 70](/us/states/al/districts/house/70.md) — 2% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
