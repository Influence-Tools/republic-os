---
type: Jurisdiction
title: "Madison County, IL"
classification: county
fips: "17119"
state: "IL"
demographics:
  population: 264238
  population_under_18: 56348
  population_18_64: 158956
  population_65_plus: 48934
  median_household_income: 75793
  poverty_rate: 11.06
  homeownership_rate: 74.2
  unemployment_rate: 4.59
  median_home_value: 173000
  gini_index: 0.4409
  vacancy_rate: 7.58
  race_white: 219413
  race_black: 20666
  race_asian: 2245
  race_native: 500
  hispanic: 11399
  bachelors_plus: 78034
districts:
  - to: "us/states/il/districts/15"
    rel: in-district
    area_weight: 0.6262
  - to: "us/states/il/districts/13"
    rel: in-district
    area_weight: 0.3737
  - to: "us/states/il/districts/senate/55"
    rel: in-district
    area_weight: 0.5584
  - to: "us/states/il/districts/senate/56"
    rel: in-district
    area_weight: 0.2819
  - to: "us/states/il/districts/senate/50"
    rel: in-district
    area_weight: 0.1536
  - to: "us/states/il/districts/senate/57"
    rel: in-district
    area_weight: 0.0061
  - to: "us/states/il/districts/house/109"
    rel: in-district
    area_weight: 0.5584
  - to: "us/states/il/districts/house/111"
    rel: in-district
    area_weight: 0.1817
  - to: "us/states/il/districts/house/100"
    rel: in-district
    area_weight: 0.1536
  - to: "us/states/il/districts/house/112"
    rel: in-district
    area_weight: 0.1002
  - to: "us/states/il/districts/house/113"
    rel: in-district
    area_weight: 0.0061
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, il]
timestamp: "2026-07-03"
---

# Madison County, IL

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 264238 |
| Under 18 | 56348 |
| 18–64 | 158956 |
| 65+ | 48934 |
| Median household income | 75793 |
| Poverty rate | 11.06 |
| Homeownership rate | 74.2 |
| Unemployment rate | 4.59 |
| Median home value | 173000 |
| Gini index | 0.4409 |
| Vacancy rate | 7.58 |
| White | 219413 |
| Black | 20666 |
| Asian | 2245 |
| Native | 500 |
| Hispanic/Latino | 11399 |
| Bachelor's or higher | 78034 |

## Districts

- [IL-15](/us/states/il/districts/15.md) — 63% (congressional)
- [IL-13](/us/states/il/districts/13.md) — 37% (congressional)
- [IL Senate District 55](/us/states/il/districts/senate/55.md) — 56% (state senate)
- [IL Senate District 56](/us/states/il/districts/senate/56.md) — 28% (state senate)
- [IL Senate District 50](/us/states/il/districts/senate/50.md) — 15% (state senate)
- [IL Senate District 57](/us/states/il/districts/senate/57.md) — 1% (state senate)
- [IL House District 109](/us/states/il/districts/house/109.md) — 56% (state house)
- [IL House District 111](/us/states/il/districts/house/111.md) — 18% (state house)
- [IL House District 100](/us/states/il/districts/house/100.md) — 15% (state house)
- [IL House District 112](/us/states/il/districts/house/112.md) — 10% (state house)
- [IL House District 113](/us/states/il/districts/house/113.md) — 1% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
