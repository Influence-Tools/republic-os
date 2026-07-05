---
type: Jurisdiction
title: "Collin County, TX"
classification: county
fips: "48085"
state: "TX"
demographics:
  population: 1163337
  population_under_18: 287584
  population_18_64: 741039
  population_65_plus: 134714
  median_household_income: 121600
  poverty_rate: 6.23
  homeownership_rate: 64.52
  unemployment_rate: 4.17
  median_home_value: 475600
  gini_index: 0.4306
  vacancy_rate: 4.74
  race_white: 621943
  race_black: 127684
  race_asian: 218741
  race_native: 5198
  hispanic: 187150
  bachelors_plus: 606798
districts:
  - to: "us/states/tx/districts/03"
    rel: in-district
    area_weight: 0.8069
  - to: "us/states/tx/districts/04"
    rel: in-district
    area_weight: 0.1711
  - to: "us/states/tx/districts/32"
    rel: in-district
    area_weight: 0.0219
  - to: "us/states/tx/districts/senate/8"
    rel: in-district
    area_weight: 0.9288
  - to: "us/states/tx/districts/senate/30"
    rel: in-district
    area_weight: 0.0505
  - to: "us/states/tx/districts/senate/2"
    rel: in-district
    area_weight: 0.0206
  - to: "us/states/tx/districts/house/67"
    rel: in-district
    area_weight: 0.3757
  - to: "us/states/tx/districts/house/89"
    rel: in-district
    area_weight: 0.2454
  - to: "us/states/tx/districts/house/66"
    rel: in-district
    area_weight: 0.1597
  - to: "us/states/tx/districts/house/61"
    rel: in-district
    area_weight: 0.1503
  - to: "us/states/tx/districts/house/70"
    rel: in-district
    area_weight: 0.0412
  - to: "us/states/tx/districts/house/33"
    rel: in-district
    area_weight: 0.0277
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, tx]
timestamp: "2026-07-03"
---

# Collin County, TX

County jurisdiction — 9 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 1163337 |
| Under 18 | 287584 |
| 18–64 | 741039 |
| 65+ | 134714 |
| Median household income | 121600 |
| Poverty rate | 6.23 |
| Homeownership rate | 64.52 |
| Unemployment rate | 4.17 |
| Median home value | 475600 |
| Gini index | 0.4306 |
| Vacancy rate | 4.74 |
| White | 621943 |
| Black | 127684 |
| Asian | 218741 |
| Native | 5198 |
| Hispanic/Latino | 187150 |
| Bachelor's or higher | 606798 |

## Districts

- [TX-03](/us/states/tx/districts/03.md) — 81% (congressional)
- [TX-04](/us/states/tx/districts/04.md) — 17% (congressional)
- [TX-32](/us/states/tx/districts/32.md) — 2% (congressional)
- [TX Senate District 8](/us/states/tx/districts/senate/8.md) — 93% (state senate)
- [TX Senate District 30](/us/states/tx/districts/senate/30.md) — 5% (state senate)
- [TX Senate District 2](/us/states/tx/districts/senate/2.md) — 2% (state senate)
- [TX House District 67](/us/states/tx/districts/house/67.md) — 38% (state house)
- [TX House District 89](/us/states/tx/districts/house/89.md) — 25% (state house)
- [TX House District 66](/us/states/tx/districts/house/66.md) — 16% (state house)
- [TX House District 61](/us/states/tx/districts/house/61.md) — 15% (state house)
- [TX House District 70](/us/states/tx/districts/house/70.md) — 4% (state house)
- [TX House District 33](/us/states/tx/districts/house/33.md) — 3% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
