---
type: Jurisdiction
title: "Monmouth County, NJ"
classification: county
fips: "34025"
state: "NJ"
demographics:
  population: 645353
  population_under_18: 134746
  population_18_64: 387237
  population_65_plus: 123370
  median_household_income: 124845
  poverty_rate: 6.49
  homeownership_rate: 75.55
  unemployment_rate: 5.4
  median_home_value: 606100
  gini_index: 0.4723
  vacancy_rate: 6.92
  race_white: 480349
  race_black: 38675
  race_asian: 35205
  race_native: 3886
  hispanic: 83325
  bachelors_plus: 326685
districts:
  - to: "us/states/nj/districts/04"
    rel: in-district
    area_weight: 0.3347
  - to: "us/states/nj/districts/03"
    rel: in-district
    area_weight: 0.2874
  - to: "us/states/nj/districts/06"
    rel: in-district
    area_weight: 0.113
  - to: "us/states/nj/districts/senate/11"
    rel: in-district
    area_weight: 0.198
  - to: "us/states/nj/districts/senate/13"
    rel: in-district
    area_weight: 0.1973
  - to: "us/states/nj/districts/senate/12"
    rel: in-district
    area_weight: 0.1828
  - to: "us/states/nj/districts/senate/30"
    rel: in-district
    area_weight: 0.1442
  - to: "us/states/nj/districts/senate/10"
    rel: in-district
    area_weight: 0.0118
  - to: "us/states/nj/districts/house/11"
    rel: in-district
    area_weight: 0.198
  - to: "us/states/nj/districts/house/13"
    rel: in-district
    area_weight: 0.1973
  - to: "us/states/nj/districts/house/12"
    rel: in-district
    area_weight: 0.1828
  - to: "us/states/nj/districts/house/30"
    rel: in-district
    area_weight: 0.1442
  - to: "us/states/nj/districts/house/10"
    rel: in-district
    area_weight: 0.0118
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, nj]
timestamp: "2026-07-03"
---

# Monmouth County, NJ

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 645353 |
| Under 18 | 134746 |
| 18–64 | 387237 |
| 65+ | 123370 |
| Median household income | 124845 |
| Poverty rate | 6.49 |
| Homeownership rate | 75.55 |
| Unemployment rate | 5.4 |
| Median home value | 606100 |
| Gini index | 0.4723 |
| Vacancy rate | 6.92 |
| White | 480349 |
| Black | 38675 |
| Asian | 35205 |
| Native | 3886 |
| Hispanic/Latino | 83325 |
| Bachelor's or higher | 326685 |

## Districts

- [NJ-04](/us/states/nj/districts/04.md) — 33% (congressional)
- [NJ-03](/us/states/nj/districts/03.md) — 29% (congressional)
- [NJ-06](/us/states/nj/districts/06.md) — 11% (congressional)
- [NJ Senate District 11](/us/states/nj/districts/senate/11.md) — 20% (state senate)
- [NJ Senate District 13](/us/states/nj/districts/senate/13.md) — 20% (state senate)
- [NJ Senate District 12](/us/states/nj/districts/senate/12.md) — 18% (state senate)
- [NJ Senate District 30](/us/states/nj/districts/senate/30.md) — 14% (state senate)
- [NJ Senate District 10](/us/states/nj/districts/senate/10.md) — 1% (state senate)
- [NJ House District 11](/us/states/nj/districts/house/11.md) — 20% (state house)
- [NJ House District 13](/us/states/nj/districts/house/13.md) — 20% (state house)
- [NJ House District 12](/us/states/nj/districts/house/12.md) — 18% (state house)
- [NJ House District 30](/us/states/nj/districts/house/30.md) — 14% (state house)
- [NJ House District 10](/us/states/nj/districts/house/10.md) — 1% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
